from _2023.day11 import Universe

from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    universe = Universe.from_input(data)

    total = 0
    for (a, b) in universe.galaxy_pairs:
        distance = universe.compute_expanded_distance_between_points(a, b)
        total += distance

    return total


if __name__ == "__main__":
    print(compute_solution(load_input(11)))
