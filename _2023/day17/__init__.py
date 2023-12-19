from dataclasses import dataclass
from enum import Enum
from typing import Optional
from functools import cache, cached_property

Position = tuple[int, int]
Distance = int
Tiles = list[list[Distance]]


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    RIGHT = ">"
    LEFT = "<"

    @property
    def opposite(self) -> "Direction":
        return OPPOSITE_MAPPING[self]

    @classmethod
    def from_two_points(cls, start: Position, end: Position) -> "Direction":
        x_start, y_start = start
        x_end, y_end = end
        if x_start == x_end and y_start == y_end:
            raise RuntimeError("Cannot compute direction for the same point")
        elif x_start == x_end:
            if y_start < y_end:
                return Direction.DOWN
            else:
                return Direction.UP
        elif y_start == y_end:
            if x_start < x_end:
                return Direction.RIGHT
            else:
                return Direction.LEFT
        else:
            raise RuntimeError(
                "Cannot compute direction for points that are not close-by"
            )


OPPOSITE_MAPPING = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.RIGHT: Direction.LEFT,
    Direction.LEFT: Direction.RIGHT,
}


@dataclass
class Node:
    position: Position
    distance_to_enter: int
    enter_direction: Optional[Direction] = None
    direction_streak: int = 1

    def __hash__(self) -> int:
        return hash(
            (
                self.position,
                self.distance_to_enter,
                self.enter_direction,
                self.direction_streak,
            )
        )

    def __eq__(self, other: "Node") -> bool:
        return self.position == other.position


@dataclass
class Map:
    tiles: list[list[int]]

    start_node: Node
    end_node: Node

    max_x: int
    max_y: int

    @cached_property
    def start_position(self) -> Position:
        return 0, 0

    @cached_property
    def end_position(self) -> Position:
        return self.max_x, self.max_y

    @classmethod
    def from_data(cls, data: str) -> "Map":
        tiles = [
            [int(character) for character in line]
            for line in data.splitlines()
        ]

        max_y = len(tiles) - 1
        max_x = len(tiles[0]) - 1

        return Map(
            tiles=tiles,
            max_x=max_x,
            max_y=max_y,
            start_node=Node(
                position=(0, 0), distance_to_enter=0, direction_streak=0
            ),
            end_node=Node(
                position=(max_x, max_y), distance_to_enter=tiles[max_y][max_x]
            ),
        )

    def h(self, node: Node) -> float:
        x_b, y_b = self.end_position
        x_a, y_a = node.position
        return node.distance_to_enter + abs(x_b - x_a) + abs(y_b - y_a)

    def get_distance_on(self, position: Position) -> int:
        x, y = position
        return self.tiles[y][x]

    def is_valid_position(self, position: Position) -> bool:
        x, y = position
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def get_immediate_neighbors(self, node: Node) -> list[Node]:
        x, y = node.position
        immediate_neighbors = []
        for connected_position, direction in [
            ((x + 1, y), Direction.RIGHT),
            ((x - 1, y), Direction.LEFT),
            ((x, y + 1), Direction.DOWN),
            ((x, y - 1), Direction.UP),
        ]:
            if not self.is_valid_position(connected_position):
                continue

            if (
                node.enter_direction
                and direction == node.enter_direction.opposite
            ):
                continue

            if direction == node.enter_direction:
                streak = node.direction_streak + 1
            else:
                streak = 1

            distance_to_enter = self.get_distance_on(connected_position)

            immediate_neighbors.append(
                Node(
                    position=connected_position,
                    distance_to_enter=distance_to_enter,
                    enter_direction=direction,
                    direction_streak=streak,
                )
            )

        return immediate_neighbors
