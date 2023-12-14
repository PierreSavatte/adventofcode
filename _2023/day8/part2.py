import math
from dataclasses import dataclass

from _2023.day8 import parse_input, Map
from _2023.load_input import load_input


@dataclass
class Loop:
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
            if node_key in self.map.ending_nodes:
                return Loop(length=step + 1)
            seen[node_key] = step
            step += 1


class Ghosts(list):
    def compute_steps(self):
        loops = [ghost.compute_loop() for ghost in self]
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
    print(compute_solution(load_input(8)))
