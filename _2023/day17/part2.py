import time

from _2023.day17 import Map, CrucibleType, compute_heat_loss
from _2023.day17.pathfinding import a_star
from _2023.load_input import load_input


def compute_solution(data: str, display_progress_bar: bool = False) -> int:
    map = Map.from_data(data, crucible_type=CrucibleType.ULTRA)
    path = a_star(map=map, display_progress_bar=display_progress_bar)
    return compute_heat_loss(path)


if __name__ == "__main__":
    # 514 < solution < 1404
    start = time.time()
    print(compute_solution(load_input(17), display_progress_bar=True))
    end = time.time()
    print(end - start)
