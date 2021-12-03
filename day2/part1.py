import aoc_utils

FILE = "input"

direction_to_axis_and_sign = {
    "forward": ["x", 1],
    "down": ["z", 1],
    "up": ["z", -1],
}


def parse_line(line):
    direction, value = line.split(" ")

    axis, sign = direction_to_axis_and_sign[direction]

    return axis, int(value) * sign


def parse_file(file_path):
    return aoc_utils.parse_file(file_path, line_parser=parse_line)


def resolution(instructions):
    position = {"x": 0, "z": 0}

    for instruction in instructions:
        axis, value = instruction
        position[axis] += value

    return position["x"] * position["z"]


def challenge_resolution():
    series = parse_file(FILE)
    return resolution(series)


if __name__ == "__main__":
    print(challenge_resolution())
