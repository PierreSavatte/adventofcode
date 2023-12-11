from _2023.day11 import Universe, manhattan_distance

from _2023.load_input import load_input


def compute_solution(data: str, age: int) -> int:
    universe = Universe.from_input(data)

    print("Expanding universe...")
    expanded_universe = universe.expand(age=age)

    total = 0
    pairs = expanded_universe.galaxy_pairs
    print(f"Starting computing the {len(pairs)} pairs...")
    for (a, b) in pairs:
        distance = manhattan_distance(a, b)
        total += distance

    return total


if __name__ == "__main__":
    print(compute_solution(load_input(11), age=1_000_000))
