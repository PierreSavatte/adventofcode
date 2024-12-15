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


def get_next_position(position: POSITION, direction: Direction) -> POSITION:
    delta_x, delta_y = direction.delta

    x, y = position
    return x + delta_x, y + delta_y


class Box:
    def __init__(self, *positions: POSITION):
        self.positions: list[POSITION] = list(positions)

    def get_neighbors_positions(self, direction: Direction) -> list[POSITION]:
        return [
            get_next_position(position=position, direction=direction)
            for position in self.positions
        ]

    def move(self, direction: Direction):
        self.positions = [
            get_next_position(position, direction)
            for position in self.positions
        ]

    def __eq__(self, other: "Box") -> bool:
        if not isinstance(other, Box):
            raise NotImplementedError()
        return self.positions == other.positions

    def __repr__(self) -> str:
        return f"Box({self.positions})"

    @property
    def gps_position(self) -> POSITION:
        return min(self.positions)


@dataclass
class Warehouse:
    size: MAP_SIZE
    walls: list[POSITION]
    boxes: list[Box]
    robot: POSITION
    robot_moves: list[Direction]

    @property
    def size_x(self) -> int:
        return self.size[0]

    @property
    def size_y(self) -> int:
        return self.size[1]

    def get_box_at(self, position: POSITION):
        for box in self.boxes:
            if position in box.positions:
                return box

    def in_map(self, position: POSITION) -> bool:
        x, y = position
        return 0 <= x < self.size_x and 0 <= y < self.size_y

    def to_str(self) -> str:
        map = [""]
        for y in range(self.size_y):
            line = []
            for x in range(self.size_x):
                position = (x, y)

                box = self.get_box_at(position)

                character = "."
                if position == self.robot:
                    character = "@"
                elif box:
                    character = "O"
                elif position in self.walls:
                    character = "#"

                line.append(character)
            map.append("".join(line))
        return "\n".join(map)

    def _get_all_boxes(self, box: Box, direction: Direction) -> list[Box]:
        next_boxes = []
        for position in box.get_neighbors_positions(direction=direction):
            if not self.in_map(position):
                continue

            if position in self.walls:
                raise CannotMove(f"Blocked by {position}")

            next_box = self.get_box_at(position)
            if next_box is not None:
                next_boxes.append(next_box)

        all_boxes = [box]
        for next_box in next_boxes:
            all_boxes.extend(self._get_all_boxes(next_box, direction))
        return all_boxes

    def _get_boxes_to_move(self, direction: Direction) -> list[Box]:
        delta_x, delta_y = direction.delta

        start_x = self.robot[0] + delta_x
        start_y = self.robot[1] + delta_y
        next_position = start_x, start_y

        if next_position in self.walls:
            raise CannotMove(f"Blocked by {next_position}")

        box = self.get_box_at(next_position)
        if box is not None:
            return self._get_all_boxes(box, direction)

        return []

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
                    box_to_move.move(robot_move)
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
                boxes.append(Box((x, y)))
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
