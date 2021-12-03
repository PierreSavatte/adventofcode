import os

from day1.utils import parse_file

FILE = os.path.join("", "input")


def resolution(series):
    series_copy = series[:]

    last_item = series_copy.pop(0)
    nb_increased = 0
    for item in series_copy:
        if item > last_item:
            nb_increased += 1

        last_item = item

    return nb_increased


def challenge_resolution():
    series = parse_file(FILE)
    return resolution(series)


if __name__ == "__main__":
    print(challenge_resolution())
