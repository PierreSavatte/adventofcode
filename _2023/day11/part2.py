from _2023.day11 import Universe

from _2023.load_input import load_input


def compute_solution(data: str, age: int) -> int:
    universe = Universe.from_input(data=data, age=age)

    total = 0
    pairs = universe.galaxy_pairs
    for (a, b) in pairs:
        distance = universe.compute_expanded_distance_between_points(a, b)
        total += distance

    return total


if __name__ == "__main__":
    print(compute_solution(load_input(11), age=1_000_000))
