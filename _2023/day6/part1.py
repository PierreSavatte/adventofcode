from _2023.day6 import parse_input
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    races = parse_input(data)
    solution = 1
    for race in races:
        options = race.compute_winning_options()
        margin = len(options)
        solution *= margin
    return solution


if __name__ == "__main__":
    print(compute_solution(load_input(6)))
