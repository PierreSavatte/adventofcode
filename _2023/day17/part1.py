import cProfile
import pstats
from copy import deepcopy
from typing import Optional, Callable

from _2023.day17 import Map, Node
from _2023.day17.pathfinding.a_star import a_star
from _2023.day17.pathfinding.dijkstra import dijkstra
from _2023.load_input import load_input


def build_solution_tiles(map: Map, shortest_route: list[Node]):
    tiles = deepcopy(map.tiles)
    for node in shortest_route:
        x, y = node.position
        if node.enter_direction:
            value = node.enter_direction.value
            tiles[y][x] = value

    return "\n".join(
        ["".join([str(value) for value in tiles_line]) for tiles_line in tiles]
    )


def compute_heat_loss(path: list[Node]) -> int:
    return sum(node.distance_to_enter for node in path if node.enter_direction)


def compute_solution(data: str, algorithm: Optional[Callable] = None) -> int:
    if algorithm is None:
        algorithm = a_star
    map = Map.from_data(data)
    path = algorithm(map=map)
    return compute_heat_loss(path)


def profiling():
    data = load_input(17)
    with cProfile.Profile() as pr:
        try:
            compute_solution(data, algorithm=dijkstra)
        except KeyboardInterrupt:
            ...
        finally:
            pr.dump_stats("profiling")

    stats = pstats.Stats("profiling")
    stats.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(15)


if __name__ == "__main__":
    # < 1249
    print(compute_solution(load_input(17)))
