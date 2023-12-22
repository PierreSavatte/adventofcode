import cProfile
import pstats

from _2023.day17.part2 import compute_solution
from _2023.load_input import load_input


def profiling():
    data = load_input(17)
    with cProfile.Profile() as pr:
        try:
            compute_solution(data, display_progress_bar=True)
        except KeyboardInterrupt:
            ...
        finally:
            pr.dump_stats("profiling")

    stats = pstats.Stats("profiling")
    stats.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(15)


if __name__ == "__main__":
    profiling()
