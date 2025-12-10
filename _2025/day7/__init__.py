from dataclasses import dataclass, field
from typing import Any, Optional


class Position(tuple[int, int]):
    @property
    def x(self) -> int:
        return self[0]

    @property
    def y(self) -> int:
        return self[1]

    def split(self) -> list["Position"]:
        return [Position((self.x - 1, self.y)), Position((self.x + 1, self.y))]

    def __repr__(self):
        return f"({self.x}, {self.y})"


@dataclass
class Beam:
    positions: list[Position]
    splitter_hit: Optional[Position]

    parents: list["Beam"] = field(default_factory=list)

    _timelines_nb: Optional[int] = None

    @property
    def timelines_nb(self):
        if self._timelines_nb is None:
            if not self.parents:
                return 1
            self._timelines_nb = sum(
                parent.timelines_nb for parent in self.parents
            )

        return self._timelines_nb

    def __eq__(self, other):
        if not isinstance(other, Beam):
            return False
        else:
            return any(p in self.positions for p in other.positions)

    def __repr__(self):
        return f"Beam<positions={self.positions}>"


@dataclass
class Diagram:
    width: int
    height: int
    spawn: Position
    splitters: list[Position]

    def generate_beam(self, spawn: Position) -> Beam:
        splitter_hit = None
        position_list = []
        for y in range(spawn.y, self.height):
            target = Position((spawn.x, y))
            if target in self.splitters:
                splitter_hit = target
                break
            position_list.append(target)

        return Beam(
            positions=position_list,
            splitter_hit=splitter_hit,
        )

    def count_beams_that_has_split(self) -> int:
        beams = BeamGenerator(self).generate_all_beams(self.spawn)
        return sum(beam.splitter_hit is not None for beam in beams)

    def count_total_beams_that_reached_the_bottom(self) -> int:
        beams = BeamGenerator(self, quantum_mode=True).generate_all_beams(
            self.spawn
        )
        return sum(
            beam.timelines_nb for beam in beams if beam.splitter_hit is None
        )

    def export_snapshot(
        self, beams: list[Beam], with_count: bool = False
    ) -> str:
        map = []
        for y in range(self.height):
            map.append(["." for _ in range(self.width)])

        for beam in beams:
            for position in beam.positions:
                if map[position.y][position.x] == ".":
                    map[position.y][position.x] = "|"
                else:
                    raise RuntimeError(
                        f"Error while applying beam on {position=}"
                    )
            if with_count:
                last_pos = beam.positions[-1]
                map[last_pos.y][last_pos.x] = f"{beam.timelines_nb:X}"

        for splitter in self.splitters:
            if map[splitter.y][splitter.x] == ".":
                map[splitter.y][splitter.x] = "^"
            else:
                raise RuntimeError(
                    f"Error while applying splitter on {splitter=}"
                )

        map[self.spawn.y][self.spawn.x] = "S"

        return "\n".join(["".join(line) for line in map]) + "\n"

    def export_output_map(self, with_count: bool = False) -> str:
        beams = BeamGenerator(self, quantum_mode=True).generate_all_beams(
            self.spawn
        )
        return self.export_snapshot(beams=beams, with_count=with_count)


def parse_diagram(input: str) -> Diagram:
    lines = input.strip().splitlines()

    width = len(lines[0])
    height = len(lines)

    spawn = None
    splitters = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == ".":
                continue
            elif char == "S":
                spawn = Position((x, y))
            elif char == "^":
                splitters.append(Position((x, y)))
            else:
                raise RuntimeError(f"Unsupported character: {char=}.")

    if spawn is None:
        raise RuntimeError("Spawn position not found in the diagram.")

    return Diagram(
        width=width,
        height=height,
        spawn=spawn,
        splitters=splitters,
    )


def get_index(l: list, item: Any) -> Optional[int]:
    try:
        return l.index(item)
    except ValueError:
        return None


class BeamGenerator:
    def __init__(self, diagram: Diagram, quantum_mode: bool = False):
        self.total_beams: list[Beam] = []
        self.new_beams: list[Beam] = []
        self.current_beams: list[Beam] = []

        self.diagram = diagram
        self.quantum_mode = quantum_mode

    def build_beam(
        self, spawn: Position, parent: Optional[Beam] = None
    ) -> Beam:
        splitter_hit = None
        position_list = []
        for y in range(spawn.y, self.diagram.height):
            target = Position((spawn.x, y))
            if target in self.diagram.splitters:
                splitter_hit = target
                break
            position_list.append(target)

        parents = [parent] if parent else []
        return Beam(
            positions=position_list,
            splitter_hit=splitter_hit,
            parents=parents,
        )

    def continue_generation(
        self, start_position: Position, parent: Optional[Beam] = None
    ):
        target_beam = self.build_beam(start_position, parent)
        i = get_index(self.total_beams, target_beam)
        j = get_index(self.new_beams, target_beam)

        if i is None and j is None:
            self.new_beams.append(target_beam)

        elif self.quantum_mode:
            if i is not None:
                assert j is None, "We have a problem..."
                self.total_beams[i].parents.append(parent)
            elif j is not None:
                self.new_beams[j].parents.append(parent)

    def generate_all_beams(self, spawn: Position) -> list[Beam]:
        self.continue_generation(spawn)

        while self.new_beams:
            self.total_beams.extend(self.new_beams[:])
            self.current_beams = self.new_beams[:]
            self.new_beams = []

            for beam in self.current_beams:
                if not beam.splitter_hit:
                    continue

                new_spawns = beam.splitter_hit.split()
                for new_spawn in new_spawns:
                    self.continue_generation(
                        start_position=new_spawn, parent=beam
                    )

        return self.total_beams
