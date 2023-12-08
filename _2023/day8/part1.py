from _2023.day8 import parse_input

from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    map = parse_input(data)
    return map.count_steps(starting_node="AAA", ending_node="ZZZ")


if __name__ == "__main__":
    print(compute_solution(load_input(8)))
