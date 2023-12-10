from _2023.day10 import Map
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    map = Map.from_input(data)
    return map.compute_enclosed_tiles()


if __name__ == "__main__":
    print(compute_solution(load_input(10)))
