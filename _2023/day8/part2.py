import math
from dataclasses import dataclass

from _2023.day8 import parse_input, Map
from _2023.load_input import load_input


@dataclass
class Loop:
    started_at_step: int
    length: int


@dataclass
class Ghost:
    map: Map
    starting_node: str

    def compute_loop(self) -> Loop:
        node_key = self.starting_node
        seen = {}
        step = 0
        while True:
            direction = self.map.get_instruction_at(step)
            node = self.map.tree[node_key]
            node_key = getattr(node, direction)
            if node_key in seen.keys():
                return Loop(
                    started_at_step=seen[node_key],
                    length=len(seen),
                )
            seen[node_key] = step
            step += 1


class Ghosts(list):
    def compute_steps(self):
        loops = [ghost.compute_loop() for ghost in self]
        print(loops)

        # Assumption: loops started at the same time
        started_at = loops[0].started_at_step
        assert all([loop.started_at_step == started_at for loop in loops])

        return math.lcm(*[loop.length for loop in loops])


def compute_solution(data: str) -> int:
    map = parse_input(data)
    ghosts = Ghosts(
        [
            Ghost(map=map, starting_node=starting_node)
            for starting_node in map.starting_nodes
        ]
    )
    return ghosts.compute_steps()


if __name__ == "__main__":
    # tried:
    # 52766656211
    # 8288280
    # 8451648
    print(compute_solution(load_input(8)))
