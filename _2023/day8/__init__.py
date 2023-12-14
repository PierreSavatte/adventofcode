from dataclasses import dataclass


@dataclass
class Node:
    L: str
    R: str

    def __hash__(self):
        return hash((self.L, self.R))


@dataclass
class Map:
    instructions: str
    tree: dict[str, Node]

    @property
    def total_instructions(self):
        return len(self.instructions)

    def get_instruction_at(self, step: int) -> str:
        return self.instructions[step % self.total_instructions]

    @property
    def starting_nodes(self):
        return [node for node in self.tree.keys() if node.endswith("A")]

    @property
    def ending_nodes(self):
        return [node for node in self.tree.keys() if node.endswith("Z")]

    def count_steps(self, starting_node: str, ending_node: str) -> int:
        nb_total_instructions = len(self.instructions)

        node_key = starting_node
        steps = 0
        while node_key != ending_node:
            node = self.tree[node_key]
            direction = self.instructions[steps % nb_total_instructions]
            node_key = getattr(node, direction)
            steps += 1

        return steps


def parse_input(data: str) -> Map:
    lines = data.split("\n")
    instructions = lines.pop(0)

    _ = lines.pop(0)

    tree = {}
    for line in lines:
        node_name, node = line.split(" = ")
        left, right = node.split(", ")

        tree[node_name] = Node(L=left[1:], R=right[:-1])

    return Map(instructions=instructions, tree=tree)
