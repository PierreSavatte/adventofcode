from dataclasses import dataclass
from enum import Enum
from typing import Generator

from tqdm import tqdm

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

    def get_next_position(self, position: POSITION) -> POSITION:
        delta_x, delta_y = self.delta
        x, y = position
        return x + delta_x, y + delta_y


class Box:
    def __init__(self, *positions: POSITION):
        self.positions: list[POSITION] = list(positions)

    def get_neighbors_positions(self, direction: Direction) -> list[POSITION]:
        neighbors_positions = []
        for position in self.positions:
            next_position = direction.get_next_position(position)
            if next_position not in self.positions:
                neighbors_positions.append(next_position)

        return neighbors_positions

    def move(self, direction: Direction):
        self.positions = [
            direction.get_next_position(position)
            for position in self.positions
        ]

    @property
    def gps_position(self) -> POSITION:
        return min(self.positions)

    @property
    def display_characters(self) -> list[str]:
        if len(self.positions) == 2:
            return ["[", "]"]
        else:
            return ["O" for _ in range(len(self.positions))]

    def __eq__(self, other: "Box") -> bool:
        if not isinstance(other, Box):
            raise NotImplementedError()
        return self.positions == other.positions

    def __hash__(self):
        return hash(tuple(self.positions))

    def __repr__(self) -> str:
        return f"Box({self.positions})"


@dataclass
class Warehouse:
    size: MAP_SIZE
    walls: list[POSITION]
    boxes: list[Box]
    robot: POSITION
    robot_moves: list[Direction]

    is_large: bool = False

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
        map = []
        for y in range(self.size_y):
            line = ["." for _ in range(self.size_x)]
            map.append(line)

        x, y = self.robot
        map[y][x] = "@"
        for wall in self.walls:
            x, y = wall
            map[y][x] = "#"

        for box in self.boxes:
            x, y = box.gps_position
            for i, character in enumerate(box.display_characters):
                map[y][x + i] = character

        display_map = [""]
        for line in map:
            display_map.append("".join(line))
        return "\n".join(display_map)

    def _get_all_boxes(self, box: Box, direction: Direction) -> set[Box]:
        next_boxes = []
        for next_position in box.get_neighbors_positions(direction=direction):
            if not self.in_map(next_position):
                raise CannotMove(f"Would go out of the map")

            if next_position in self.walls:
                raise CannotMove(f"Blocked by {next_position}")

            next_box = self.get_box_at(next_position)
            if next_box is not None:
                if next_box not in next_boxes:
                    next_boxes.append(next_box)

        all_boxes = {box}
        for next_box in next_boxes:
            all_boxes.update(self._get_all_boxes(next_box, direction))
        return all_boxes

    def _get_boxes_to_move(self, direction: Direction) -> set[Box]:
        delta_x, delta_y = direction.delta

        start_x = self.robot[0] + delta_x
        start_y = self.robot[1] + delta_y
        next_position = start_x, start_y

        if next_position in self.walls:
            raise CannotMove(f"Blocked by {next_position}")

        box = self.get_box_at(next_position)
        if box is not None:
            return self._get_all_boxes(box, direction)

        return set()

    def run(self) -> Generator[None, None, None]:
        progress_bar = tqdm(total=len(self.robot_moves))
        for i, robot_move in enumerate(self.robot_moves):

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

            progress_bar.update(1)
            yield
        progress_bar.close()

    def check_collisions(self):
        for box in self.boxes:
            found = 0
            for other_box in self.boxes:
                if box == other_box:
                    found += 1
            if found > 1:
                raise RuntimeError(f"The box {box} is colliding another box!")

            for wall in self.walls:
                if wall in box.positions:
                    raise RuntimeError(
                        f"The box {box} is colliding a wall ({wall})!"
                    )


def parse_input(data: str, large: bool = False) -> Warehouse:
    data = data.strip("\n")

    map, moves = data.split("\n\n")

    walls = []
    boxes = []
    robot = None
    lines = map.split("\n")
    for y, line in enumerate(lines):
        x = 0
        for character in line:
            if large:
                positions = [(x, y), (x + 1, y)]
            else:
                positions = [(x, y)]
            if character == "#":
                walls.extend(positions)

            if character == "O":
                boxes.append(Box(*positions))

            if character == "@":
                robot = (x, y)

            if large:
                x += 2
            else:
                x += 1
    if robot is None:
        raise RuntimeError(
            "Didn't find the robot position when parsing input."
        )

    robot_moves = [Direction(move) for move in moves if move != "\n"]

    size_x = len(lines)
    if large:
        size_x *= 2
    size_y = len(lines[0])

    return Warehouse(
        size=(size_x, size_y),
        walls=walls,
        boxes=boxes,
        robot=robot,
        robot_moves=robot_moves,
        is_large=large,
    )


def to_gps(position: POSITION) -> int:
    x, y = position
    return 100 * y + x
