from _2023.day6 import Race
from _2023.load_input import load_input


def parse_input(data: str) -> list[Race]:
    time_line, distance_line = data.split("\n")
    _, *times_str = time_line.split()
    _, *distances_str = distance_line.split()
    races = []
    for time_str, distance_str in zip(times_str, distances_str):
        races.append(Race(time=int(time_str), min_distance=int(distance_str)))

    return races


def compute_solution(data: str) -> int:
    races = parse_input(data)
    solution = 1
    for race in races:
        options = race.compute_winning_options()
        margin = len(options)
        solution *= margin
    return solution


if __name__ == "__main__":
    print(compute_solution(load_input(6)))
