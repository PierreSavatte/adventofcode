from dataclasses import dataclass
from enum import Enum, auto
from functools import cached_property
from typing import Optional

from colorama import Fore
from colorama import Style
from colorama import init as colorama_init

Position = tuple[int, int]
Distance = int
Tiles = list[list[Distance]]
Streak = int

colorama_init()


class CrucibleType(Enum):
    REGULAR = auto()
    ULTRA = auto()


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    RIGHT = ">"
    LEFT = "<"

    @property
    def colorized(self):
        return f"{Fore.GREEN}{self.value}{Style.RESET_ALL}"

    @property
    def opposite(self) -> "Direction":
        return OPPOSITE_MAPPING[self]

    @classmethod
    def all_except(cls, other: "Direction") -> list["Direction"]:
        return [
            Direction[direction]
            for direction in Direction.__members__
            if Direction[direction] != other
        ]

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


NEW_POSITION_FUNCTION_MAPPING = {
    Direction.RIGHT: lambda x, y: (x + 1, y),
    Direction.DOWN: lambda x, y: (x, y + 1),
    Direction.LEFT: lambda x, y: (x - 1, y),
    Direction.UP: lambda x, y: (x, y - 1),
}


@dataclass
class Node:
    position: Position
    distance_to_enter: int
    enter_direction: Optional[Direction]
    direction_streak: int = 1

    def __hash__(self) -> int:
        return hash((self.position, self.enter_direction))


@dataclass
class Map:
    tiles: list[list[int]]

    start_node: Node

    max_x: int
    max_y: int

    crucible_type: CrucibleType

    @cached_property
    def start_position(self) -> Position:
        return 0, 0

    @cached_property
    def end_position(self) -> Position:
        return self.max_x, self.max_y

    @classmethod
    def from_data(
        cls, data: str, crucible_type: CrucibleType = CrucibleType.REGULAR
    ) -> "Map":
        tiles = [
            [int(character) for character in line]
            for line in data.splitlines()
        ]

        max_y = len(tiles) - 1
        max_x = len(tiles[0]) - 1

        if crucible_type == CrucibleType.REGULAR:
            map_class = Map
        else:
            map_class = UltraMap

        return map_class(
            tiles=tiles,
            max_x=max_x,
            max_y=max_y,
            crucible_type=crucible_type,
            start_node=Node(
                position=(0, 0),
                distance_to_enter=0,
                direction_streak=0,
                enter_direction=None,
            ),
        )

    def h(self, node: Node) -> float:
        x_b, y_b = self.end_position
        x_a, y_a = node.position
        return abs(x_b - x_a) + abs(y_b - y_a)

    def get_distance_on(self, position: Position) -> int:
        x, y = position
        return self.tiles[y][x]

    def is_valid_position(self, position: Position) -> bool:
        x, y = position
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def get_neighbors(self, node: Node) -> list[tuple[Node, dict[Node, Node]]]:
        x, y = node.position
        immediate_neighbors = []
        for connected_position, direction in [
            ((x + 1, y), Direction.RIGHT),
            ((x, y + 1), Direction.DOWN),
            ((x - 1, y), Direction.LEFT),
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

            if streak >= 4:
                continue

            distance_to_enter = self.get_distance_on(connected_position)

            additional_came_from: dict[Node, Node] = {}

            immediate_neighbors.append(
                (
                    Node(
                        position=connected_position,
                        distance_to_enter=distance_to_enter,
                        enter_direction=direction,
                        direction_streak=streak,
                    ),
                    additional_came_from,
                )
            )

        return immediate_neighbors


class UltraMap(Map):
    def get_neighbors(self, node: Node) -> list[tuple[Node, dict[Node, Node]]]:
        x, y = node.position
        immediate_neighbors = []
        additional_came_from: dict[Node, Node] = {}

        accepted_positions = [
            ((x, y + 1), Direction.DOWN),
            ((x + 1, y), Direction.RIGHT),
            ((x - 1, y), Direction.LEFT),
            ((x, y - 1), Direction.UP),
        ]
        if node.enter_direction:
            if node.direction_streak < 4:
                new_position_function = NEW_POSITION_FUNCTION_MAPPING[
                    node.enter_direction
                ]
                new_position = new_position_function(*node.position)
                accepted_positions = [(new_position, node.enter_direction)]
            elif node.direction_streak >= 10:
                accepted_directions = Direction.all_except(
                    node.enter_direction
                )
                accepted_positions = []
                for direction in accepted_directions:
                    new_position_function = NEW_POSITION_FUNCTION_MAPPING[
                        direction
                    ]
                    accepted_positions.append(
                        (new_position_function(*node.position), direction)
                    )

        for connected_position, direction in accepted_positions:
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

            if connected_position == self.end_position and streak < 4:
                continue

            immediate_neighbors.append(
                (
                    Node(
                        position=connected_position,
                        distance_to_enter=distance_to_enter,
                        enter_direction=direction,
                        direction_streak=streak,
                    ),
                    additional_came_from,
                )
            )

        return immediate_neighbors


def build_solution_tiles(
    map: Map, shortest_route: list[Node], colorized: bool = False
) -> str:
    tiles = [[str(char) for char in tiles_line] for tiles_line in map.tiles]
    for node in shortest_route:
        x, y = node.position
        if node.enter_direction:
            if colorized:
                value = node.enter_direction.colorized
            else:
                value = node.enter_direction.value
            tiles[y][x] = value

    return "\n".join(
        ["".join([value for value in tiles_line]) for tiles_line in tiles]
    )


def compute_heat_loss(path: list[Node]) -> int:
    return sum(node.distance_to_enter for node in path if node.enter_direction)
