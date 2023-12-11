from _2023.day11 import Universe, manhattan_distance

from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    universe = Universe.from_input(data)

    expanded_universe = universe.expand()

    total = 0
    for (a, b) in expanded_universe.galaxy_pairs:
        distance = manhattan_distance(a, b)
        total += distance

    return total


if __name__ == "__main__":
    print(compute_solution(load_input(11)))
