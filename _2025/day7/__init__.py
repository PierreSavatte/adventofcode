from dataclasses import dataclass
from typing import Optional


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
        return sum(beam.splitter_hit is None for beam in beams)

    def export_output_map(self) -> str:
        map = []
        for y in range(self.height):
            map.append(["." for _ in range(self.width)])

        beams = BeamGenerator(self).generate_all_beams(self.spawn)

        for beam in beams:
            for position in beam.positions:
                if map[position.y][position.x] == ".":
                    map[position.y][position.x] = "|"
                else:
                    raise RuntimeError(
                        f"Error while applying beam on {position=}"
                    )

        for splitter in self.splitters:
            if map[splitter.y][splitter.x] == ".":
                map[splitter.y][splitter.x] = "^"
            else:
                raise RuntimeError(
                    f"Error while applying splitter on {splitter=}"
                )

        map[self.spawn.y][self.spawn.x] = "S"

        return "\n".join(["".join(line) for line in map]) + "\n"


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


class BeamGenerator:
    def __init__(self, diagram: Diagram, quantum_mode: bool = False):
        self.total_beams: list[Beam] = []
        self.new_beams: list[Beam] = []
        self.current_beams: list[Beam] = []

        self.diagram = diagram
        self.quantum_mode = quantum_mode

    def generate_beam(self, spawn: Position) -> Beam:
        splitter_hit = None
        position_list = []
        for y in range(spawn.y, self.diagram.height):
            target = Position((spawn.x, y))
            if target in self.diagram.splitters:
                splitter_hit = target
                break
            position_list.append(target)

        new_beam = Beam(
            positions=position_list,
            splitter_hit=splitter_hit,
        )

        if self.quantum_mode or (
            new_beam not in self.total_beams and new_beam not in self.new_beams
        ):
            self.new_beams.append(new_beam)

    def generate_all_beams(self, spawn: Position) -> list[Beam]:
        self.generate_beam(spawn)

        while self.new_beams:
            self.total_beams.extend(self.new_beams[:])
            self.current_beams = self.new_beams[:]
            self.new_beams = []

            for beam in self.current_beams:
                if not beam.splitter_hit:
                    continue

                new_spawns = beam.splitter_hit.split()
                for new_spawn in new_spawns:
                    self.generate_beam(new_spawn)

        return self.total_beams
