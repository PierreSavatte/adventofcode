from dataclasses import dataclass


@dataclass
class Node:
    L: str
    R: str


@dataclass
class Map:
    instructions: str
    tree: dict[str, Node]


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
