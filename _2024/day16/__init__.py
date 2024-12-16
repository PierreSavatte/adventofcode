from dataclasses import dataclass
from typing import Any

from _2024.day10.a_star import Direction, a_star, euclidean_distance

POSITION = tuple[int, int]


def compute_distance(
    current: POSITION,
    current_direction: Direction,
    neighbor: POSITION,
) -> int:
    new_direction = Direction.from_two_points(current, neighbor)
    nb_rotations = current_direction.get_nb_90_rotation(new_direction)
    distance = euclidean_distance(current, neighbor)
    return distance + 1000 * nb_rotations


def compute_total_distance(path: list[POSITION]) -> int:
    distance = 0
    current_direction = Direction.RIGHT
    for current, neighbor in zip(path, path[1:]):
        distance += compute_distance(
            current=current,
            current_direction=current_direction,
            neighbor=neighbor,
        )
        current_direction = Direction.from_two_points(current, neighbor)
    return distance


@dataclass
class Map:
    map: list[str]
    start: POSITION
    end: POSITION

    @property
    def width(self) -> int:
        return len(self.map[0])

    @property
    def height(self) -> int:
        return len(self.map)

    def in_map(self, position: POSITION) -> bool:
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    @staticmethod
    def f_function(position: POSITION, end_position: POSITION) -> int:
        x, y = position
        x_end, y_end = end_position

        delta_x = abs(x_end - x)
        delta_y = abs(y_end - y)

        return delta_x ** 2 + delta_y ** 2

    def get_neighbors(
        self, map: Any, current: POSITION, direction: Direction
    ) -> list[POSITION]:
        x, y = current
        neighbors = []
        for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = x + delta_x
            new_y = y + delta_y

            character = self.map[new_y][new_x]
            new_position = new_x, new_y

            if self.in_map(new_position) and character != "#":
                neighbors.append(new_position)

        return neighbors

    def get_optimal_path(self) -> list[POSITION]:
        return a_star(
            map=self.map,
            get_neighbors=self.get_neighbors,
            start_position=self.start,
            end_position=self.end,
            distance_function=compute_distance,
        )

    def plot_path_in_map(self, path: list[POSITION]) -> str:
        map = []
        for line in self.map:
            map.append(list(line))

        for past, current in zip(path, path[1:]):
            direction = Direction.from_two_points(past, current)
            x, y = past
            map[y][x] = direction.to_str()

        map[self.start[1]][self.start[0]] = "S"
        map[self.end[1]][self.end[0]] = "E"

        plotted_map = []
        for line in map:
            plotted_map.append("".join(line))

        return "\n".join(plotted_map)


def parse_input(data: str) -> Map:
    data = data.strip("\n")

    map = []
    start = None
    end = None
    for y, line in enumerate(data.split("\n")):
        for x, character in enumerate(line):
            if character == "S":
                start = (x, y)
            elif character == "E":
                end = (x, y)
        map.append(line.replace("S", ".").replace("E", "."))

    if not start:
        raise RuntimeError(
            "Did not find start position while parsing the map."
        )
    if not end:
        raise RuntimeError("Did not find end position while parsing the map.")

    return Map(map=map, start=start, end=end)
