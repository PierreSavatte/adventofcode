from _2023.day12 import compute_total_arrangements
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    return sum(
        compute_total_arrangements(input_line)
        for input_line in data.splitlines()
    )


if __name__ == "__main__":
    print(compute_solution(load_input(12)))
