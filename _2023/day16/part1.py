from _2023.day16 import Contraption
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    contraption = Contraption.from_data(data)
    energized_positions = contraption.compute_energized_positions()
    return len(set(energized_positions))


if __name__ == "__main__":
    print(compute_solution(load_input(16)))
