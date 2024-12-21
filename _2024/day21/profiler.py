import cProfile
import pstats

from _2024.day21.part1 import compute_solution


def part_solution():
    typing_sequences = {"246A", "965A", "780A", "638A", "803A"}
    try:
        compute_solution(typing_sequences)
    except KeyboardInterrupt:
        return


def run_profiler():
    cProfile.run("part_solution()", "stats")


def show_profiler_results():
    stats = pstats.Stats("stats")
    stats.sort_stats("cumtime").print_stats()


if __name__ == "__main__":
    # run_profiler()
    show_profiler_results()
