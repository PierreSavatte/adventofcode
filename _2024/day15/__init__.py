from dataclasses import dataclass
from enum import Enum
from typing import Generator

POSITION = tuple[int, int]
DELTA_POSITION = tuple[int, int]
MAP_SIZE = tuple[int, int]


class CannotMove(Exception):
    ...


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    RIGHT = ">"
    LEFT = "<"

    @property
    def delta(self) -> DELTA_POSITION:
        mapping = {
            Direction.UP: (0, -1),
            Direction.DOWN: (0, 1),
            Direction.RIGHT: (1, 0),
            Direction.LEFT: (-1, 0),
        }
        return mapping[self]


@dataclass
class Warehouse:
    size: MAP_SIZE
    walls: list[POSITION]
    boxes: list[POSITION]
    robot: POSITION
    robot_moves: list[Direction]

    @property
    def size_x(self) -> int:
        return self.size[0]

    @property
    def size_y(self) -> int:
        return self.size[1]

    def to_str(self) -> str:
        map = [""]
        for y in range(self.size_y):
            line = []
            for x in range(self.size_x):
                position = (x, y)

                character = "."
                if position == self.robot:
                    character = "@"
                elif position in self.boxes:
                    character = "O"
                elif position in self.walls:
                    character = "#"

                line.append(character)
            map.append("".join(line))
        return "\n".join(map)

    def _get_boxes_to_move(self, direction: Direction) -> list[POSITION]:
        delta_x, delta_y = direction.delta

        start_x = self.robot[0] + delta_x
        start_y = self.robot[1] + delta_y

        if direction == direction.UP:
            x_range = range(start_x, start_x + 1)
            y_range = range(start_y, -1, delta_y)
        elif direction == direction.DOWN:
            x_range = range(start_x, start_x + 1)
            y_range = range(start_y, self.size_y, delta_y)
        elif direction == direction.RIGHT:
            x_range = range(start_x, self.size_x, delta_x)
            y_range = range(start_y, start_y + 1)
        else:
            x_range = range(start_x, -1, delta_x)
            y_range = range(start_y, start_y + 1)

        positions = []
        for x in x_range:
            for y in y_range:
                position = (x, y)

                if position in self.walls:
                    raise CannotMove(f"Blocked by {position}")
                elif position in self.boxes:
                    positions.append(position)
                else:
                    return positions

        return positions

    def run(self) -> Generator[None, None, None]:
        for robot_move in self.robot_moves:

            try:
                boxes_to_move = self._get_boxes_to_move(robot_move)
            except CannotMove:
                ...
            else:
                delta_x, delta_y = robot_move.delta

                x, y = self.robot
                self.robot = x + delta_x, y + delta_y

                for box_to_move in boxes_to_move:
                    i = self.boxes.index(box_to_move)
                    x, y = box_to_move
                    self.boxes[i] = x + delta_x, y + delta_y
            yield


def parse_input(data: str) -> Warehouse:
    data = data.strip("\n")

    map, moves = data.split("\n\n")

    walls = []
    boxes = []
    robot = None
    lines = map.split("\n")
    size_x = len(lines)
    size_y = len(lines[0])
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            if character == "#":
                walls.append((x, y))
            if character == "O":
                boxes.append((x, y))
            if character == "@":
                robot = (x, y)

    if robot is None:
        raise RuntimeError(
            "Didn't find the robot position when parsing input."
        )

    robot_moves = [Direction(move) for move in moves if move != "\n"]

    return Warehouse(
        size=(size_x, size_y),
        walls=walls,
        boxes=boxes,
        robot=robot,
        robot_moves=robot_moves,
    )


def to_gps(position: POSITION) -> int:
    x, y = position
    return 100 * y + x
