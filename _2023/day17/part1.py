import cProfile
import pstats
import time

from _2023.day17 import Map
from _2023.day17.pathfinding import a_star
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    map = Map.from_data(data)
    return a_star(map=map)


def profiling():
    data = load_input(17)
    with cProfile.Profile() as pr:
        try:
            compute_solution(data)
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
