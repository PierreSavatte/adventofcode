from _2023.day15 import compute_hash
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    return sum(compute_hash(string) for string in data.split(","))


if __name__ == "__main__":
    print(compute_solution(load_input(15)))
