from _2023.day5 import Almanach
from _2023.load_input import load_input


def compute_solution(data: str):
    almanach = Almanach.from_input(data)

    locations = []
    for seed in almanach.seeds:
        location = almanach.map(seed)
        locations.append(location)

    return min(locations)


if __name__ == "__main__":
    print(compute_solution(load_input(5)))
