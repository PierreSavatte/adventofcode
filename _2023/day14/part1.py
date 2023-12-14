from _2023.day14 import Platform
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    platform = Platform.from_input(data)
    tilted_platform = platform.tilt_north()
    return tilted_platform.compute_load()


if __name__ == "__main__":
    print(compute_solution(load_input(14)))
