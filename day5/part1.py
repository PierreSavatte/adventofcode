import aoc_utils

FILE = "input"


def parse_file(file_path):
    def line_parser(line):
        line = line.strip("\n")

        start, end = line.split(" -> ")

        x1, y1 = start.split(",")
        x2, y2 = end.split(",")

        return [(int(x1), int(y1)), (int(x2), int(y2))]

    return aoc_utils.parse_file(file_path, line_parser)


def _compute_points(x_1, y_1, x_2, y_2):
    if x_2 != x_1:
        slope = (y_2 - y_1) / (x_2 - x_1)
        y_intercept = (x_1 * y_2 - x_2 * y_1) / (x_1 - x_2)
    else:
        slope = 1
        y_intercept = y_1

    x_increment = 1 if x_1 < x_2 else -1
    for x in range(x_1, x_2 + x_increment, x_increment):
        yield x, int(x * slope + y_intercept)


def compute_points_on_line(start, end):
    x_1, y_1 = start
    x_2, y_2 = end
    if not (x_1 == x_2 or y_1 == y_2):
        raise NotImplementedError()
    return _compute_points(x_1, y_1, x_2, y_2)


class Diagram:
    def __init__(self, x_size=10, y_size=10):
        self.x_size = x_size
        self.y_size = y_size
        self.diagram = self._init_diagram(x_size, y_size)

    @staticmethod
    def _init_diagram(x_size, y_size):
        return [[0 for y in range(y_size)] for x in range(x_size)]

    def apply_points(self, points):
        for x, y in points:
            self.diagram[y][x] += 1

    def compute_score(self):
        score = 0
        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.diagram[y][x] > 1:
                    score += 1

        return score


def resolution(lines, size_diagram=10):
    diagram = Diagram(x_size=size_diagram, y_size=size_diagram)
    for start, end in lines:
        try:
            points = compute_points_on_line(start, end)
        except NotImplementedError:
            # For now, only consider horizontal and vertical lines
            points = []
        diagram.apply_points(points)

    return diagram.compute_score()


def challenge_resolution():
    lines = parse_file(FILE)
    return resolution(lines, size_diagram=1000)


if __name__ == "__main__":
    print(challenge_resolution())
