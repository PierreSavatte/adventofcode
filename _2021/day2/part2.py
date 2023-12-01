from _2021.day2.part1 import parse_file

FILE = "input"


def resolution(instructions):
    position = {"x": 0, "z": 0, "aim": 0}

    for instruction in instructions:
        axis, value = instruction

        if axis == "z":
            axis = "aim"

        position[axis] += value

        if axis == "x":
            position["z"] += value * position["aim"]

    return position["x"] * position["z"]


def challenge_resolution():
    series = parse_file(FILE)
    return resolution(series)


if __name__ == "__main__":
    print(challenge_resolution())
