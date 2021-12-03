from day1.utils import parse_file
from day1.part1 import resolution as part1_resolution
import os

FILE = os.path.join("", "input")


def compute_window(series):
    return [
        series[i] + series[i + 1] + series[i + 2]
        for i in range(len(series) - 2)
    ]


def challenge_resolution():
    series = parse_file(FILE)
    windowed_series = compute_window(series)
    return part1_resolution(windowed_series)


if __name__ == "__main__":
    print(challenge_resolution())
