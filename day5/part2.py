from day5.part1 import (
    parse_file,
    Diagram,
    _compute_points,
    _compute_points_on_vertical_line,
)

FILE = "input"


def compute_points_on_line(start, end):
    x_1, y_1 = start
    x_2, y_2 = end
    if x_1 == x_2:
        return list(_compute_points_on_vertical_line(x_1, y_1, y_2))
    else:
        return list(_compute_points(x_1, y_1, x_2, y_2))


def resolution(lines, size_diagram=10):
    diagram = Diagram(x_size=size_diagram, y_size=size_diagram)
    for start, end in lines:
        points = compute_points_on_line(start, end)
        diagram.apply_points(points)

    return diagram.compute_score()


def challenge_resolution():
    lines = parse_file(FILE)
    return resolution(lines, size_diagram=1000)


if __name__ == "__main__":
    print(challenge_resolution())
