from _2023.day9 import Sequence
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    sequences = []
    for line in data.splitlines():
        values = map(int, line.split())
        sequences.append(Sequence(values))
    return sum(sequence.get_previous_value() for sequence in sequences)


if __name__ == "__main__":
    print(compute_solution(load_input(9)))
