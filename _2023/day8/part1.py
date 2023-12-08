from _2023.day8 import parse_input

from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    map = parse_input(data)

    node_key = "AAA"
    steps = 0
    while node_key != "ZZZ" or steps > 1_000_000:
        node = map.tree[node_key]
        direction = map.instructions[steps % len(map.instructions)]
        node_key = getattr(node, direction)
        steps += 1

    return steps


if __name__ == "__main__":
    print(compute_solution(load_input(8)))
