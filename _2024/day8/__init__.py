from collections import defaultdict
from itertools import combinations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"<Point x={self.x} y={self.y}>"

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __hash__(self):
        return (self.x, self.y).__hash__()

    def reflection_from(self, other: "Point"):
        # https://en.wikipedia.org/wiki/Point_reflection#Point_reflection_in_analytic_geometry
        return Point(2 * other.x - self.x, 2 * other.y - self.y)


class Map:
    def __init__(self, size: int, antennas: dict[str, list[Point]]):
        self.size = size
        self.antennas = antennas

    def __repr__(self) -> str:
        return f"<Map size={self.size} antennas={self.antennas}>"

    def __eq__(self, other: "Map") -> bool:
        return self.size == other.size and self.antennas == other.antennas

    def in_map(self, point: Point) -> bool:
        return 0 <= point.x < self.size and 0 <= point.y < self.size

    def compute_antinodes(self) -> dict[str, list[Point]]:
        antinodes = {}
        for antenna_type, antennas in self.antennas.items():
            antinodes_for_this_type = []
            for a, b in combinations(antennas, 2):
                for potential_antinode in [
                    a.reflection_from(b),
                    b.reflection_from(a),
                ]:
                    if self.in_map(potential_antinode):
                        antinodes_for_this_type.append(potential_antinode)
            antinodes[antenna_type] = sorted(antinodes_for_this_type)
        return antinodes


def parse_input(data: str) -> Map:
    data = data.strip("\n")

    lines = data.split("\n")
    size = len(lines)

    antennas = defaultdict(list)
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            if character != ".":
                antennas[character].append(Point(x, y))

    return Map(size=size, antennas=dict(antennas))
