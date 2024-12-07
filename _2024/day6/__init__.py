from enum import Enum
from itertools import product
from typing import Generator, Optional

POSITION = tuple[int, int]


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def turn_90_degrees(self) -> "Direction":
        mapping_90_degrees = {
            Direction.UP: Direction.RIGHT,
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP,
        }
        return mapping_90_degrees[self]

    def get_previous_position(self, position: POSITION) -> POSITION:
        delta_x = 0
        delta_y = 0
        if self == Direction.UP:
            delta_y = 1
        elif self == Direction.RIGHT:
            delta_x = -1
        elif self == Direction.DOWN:
            delta_y = -1
        else:  # self == Direction.LEFT
            delta_x = 1

        x, y = position
        return (x + delta_x, y + delta_y)


def generate_line(
    position: POSITION, direction: Direction, map_size: int
) -> Generator:
    x, y = position

    if direction == Direction.UP:
        y_range = range(y, -1, -1)
        x_range = range(x, x + 1)
    elif direction == Direction.DOWN:
        y_range = range(y, map_size)
        x_range = range(x, x + 1)
    elif direction == Direction.LEFT:
        y_range = range(y, y + 1)
        x_range = range(x, -1, -1)
    else:  # direction == Direction.RIGHT
        y_range = range(y, y + 1)
        x_range = range(x, map_size)

    for next_position in product(x_range, y_range):
        yield next_position


class Line:
    def __init__(self, start: POSITION, end: POSITION):
        self.start = start
        self.end = end

    def compute_positions(self) -> set[POSITION]:
        x_start, y_start = self.start
        x_end, y_end = self.end
        if x_start != x_end and y_start != y_end:
            raise ValueError("The positions must be in a line.")

        if x_start == x_end:
            x = x_start
            min_y = min(y_start, y_end)
            max_y = max(y_start, y_end)
            return {(x, y) for y in range(min_y, max_y + 1)}
        if y_start == y_end:
            y = y_start
            min_x = min(x_start, x_end)
            max_x = max(x_start, x_end)
            return {(x, y) for x in range(min_x, max_x + 1)}

    def get_intersection_point(self, other: "Line") -> Optional[POSITION]:
        # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
        x1, y1 = self.start
        x2, y2 = self.end

        x3, y3 = other.start
        x4, y4 = other.end

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator == 0:
            return None

        x_intersection = (
            (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
        ) / denominator
        y_intersection = (
            (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
        ) / denominator

        return (int(x_intersection), int(y_intersection))

    def __eq__(self, other: "Line") -> bool:
        return self.start == other.start and self.end == other.end


class Map:
    def __init__(
        self,
        size: int,
        guard_starting_position: POSITION,
        obstacles: list[POSITION],
    ):
        self.size = size
        self.guard_starting_position = guard_starting_position
        self.obstacles = obstacles

    def __repr__(self) -> str:
        return (
            f"<Map guard_starting_position={self.guard_starting_position} "
            f"obstacles={self.obstacles}>"
        )

    def __eq__(self, other: "Map") -> bool:
        return (
            self.guard_starting_position == other.guard_starting_position
            and self.obstacles == other.obstacles
        )

    def is_in(self, position: POSITION) -> bool:
        return position[0] < self.size and position[1] < self.size

    def get_guard_next_obstacle(
        self, position: POSITION, direction: Direction
    ) -> POSITION:
        for potential_obstacle_position in generate_line(
            position, direction, map_size=self.size
        ):
            if potential_obstacle_position in self.obstacles:
                return potential_obstacle_position

        raise StopIteration("No obstacle in the path of the guard.")

    def get_traveling_lines(self) -> list[Line]:
        guard_direction = Direction.UP
        guard_position = self.guard_starting_position

        lines = []
        try:
            while True:
                obstacle = self.get_guard_next_obstacle(
                    guard_position, guard_direction
                )
                next_guard_position = guard_direction.get_previous_position(
                    obstacle
                )
                lines.append(Line(guard_position, next_guard_position))

                guard_position = next_guard_position
                guard_direction = guard_direction.turn_90_degrees()
        except StopIteration:
            last_line = list(
                generate_line(
                    guard_position, guard_direction, map_size=self.size
                )
            )
            last_position = last_line[-1]
            lines.append(Line(guard_position, last_position))
            return lines


def parse_input(data: str) -> Map:
    data = data.strip("\n")

    lines = data.split("\n")

    guard_starting_position = None
    obstacles = []
    for y, line in enumerate(lines):
        nb_obstacles_in_line = line.count("#")
        start = 0
        end = len(line)
        while nb_obstacles_in_line:
            x = line.find("#", start, end)

            obstacles.append((x, y))

            start = x + 1
            nb_obstacles_in_line -= 1

        if "^" in line:
            x = line.find("^")
            guard_starting_position = (x, y)

    if guard_starting_position is None:
        raise RuntimeError(
            "Guard starting position was not found during input parsing."
        )

    return Map(
        size=len(lines[0]),
        guard_starting_position=guard_starting_position,
        obstacles=obstacles,
    )