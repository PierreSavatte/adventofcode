from _2024.day3 import parse_input
from _2024.load_input import load_input

REGEX = r"mul\((\d+),(\d+)\)"


def compute_solution(groups: list[tuple[int, int]]) -> int:
    return sum(map(lambda t: t[0] * t[1], groups))


if __name__ == "__main__":
    input_data = load_input(3)
    groups = parse_input(input_data, REGEX)
    print(compute_solution(groups))
