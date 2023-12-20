import cProfile
import pstats
import time
from copy import deepcopy
from typing import Optional, Callable

from _2023.day17 import Map, Node
from _2023.day17.pathfinding.a_star import a_star
from _2023.load_input import load_input


def build_solution_tiles(
    map: Map, shortest_route: list[Node], colorized: bool = False
) -> str:
    tiles = deepcopy(map.tiles)
    for node in shortest_route:
        x, y = node.position
        if node.enter_direction:
            if colorized:
                value = node.enter_direction.colorized
            else:
                value = node.enter_direction.value
            tiles[y][x] = value

    return "\n".join(
        ["".join([str(value) for value in tiles_line]) for tiles_line in tiles]
    )


def compute_solution(data: str, algorithm: Optional[Callable] = None) -> int:
    if algorithm is None:
        algorithm = a_star
    map = Map.from_data(data)
    return algorithm(map=map)


def profiling():
    data = load_input(17)
    with cProfile.Profile() as pr:
        try:
            compute_solution(data, algorithm=a_star)
        except KeyboardInterrupt:
            ...
        finally:
            pr.dump_stats("profiling")

    stats = pstats.Stats("profiling")
    stats.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(15)


if __name__ == "__main__":
    start = time.time()
    print(compute_solution(load_input(17)))
    end = time.time()
    print(end - start)
