from _2023.day6 import Race
from _2023.load_input import load_input


def parse_input(data: str) -> Race:
    time_line, distance_line = data.split("\n")
    _, *time_txt = time_line.split()
    _, *distance_txt = distance_line.split()

    time_str = "".join(map(str.strip, time_txt))
    distance_str = "".join(map(str.strip, distance_txt))

    return Race(time=int(time_str), min_distance=int(distance_str))


def compute_solution(data: str) -> int:
    race = parse_input(data)
    options = race.compute_winning_options()
    margin = len(options)
    return margin


if __name__ == "__main__":
    print(compute_solution(load_input(6)))
