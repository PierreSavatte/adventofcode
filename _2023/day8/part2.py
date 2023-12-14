from _2023.day8 import parse_input

from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    map = parse_input(data)
    ending_nodes = map.ending_nodes

    total_instructions = len(map.instructions)
    node_keys = map.starting_nodes
    steps = 0
    while node_keys != ending_nodes:
        direction = map.instructions[steps % total_instructions]
        new_node_keys = []
        for node_key in node_keys:
            node = map.tree[node_key]
            node_key = getattr(node, direction)
            new_node_keys.append(node_key)
        node_keys = new_node_keys
        steps += 1

    return steps


if __name__ == "__main__":
    print(compute_solution(load_input(8)))
