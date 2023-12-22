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

    def new_position(self, start: Position, diff: int = 1) -> Position:
        return NEW_POSITION_FUNCTION_MAPPING[self](*start, diff=diff)


OPPOSITE_MAPPING = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.RIGHT: Direction.LEFT,
    Direction.LEFT: Direction.RIGHT,
}


NEW_POSITION_FUNCTION_MAPPING = {
    Direction.RIGHT: lambda x, y, diff: (x + diff, y),
    Direction.DOWN: lambda x, y, diff: (x, y + diff),
    Direction.LEFT: lambda x, y, diff: (x - diff, y),
    Direction.UP: lambda x, y, diff: (x, y - diff),
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

    def get_neighbors(
        self, node: Node
    ) -> list[tuple[Node, int, dict[Node, Node]]]:
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

            additional_score = 0

            immediate_neighbors.append(
                (
                    Node(
                        position=connected_position,
                        distance_to_enter=distance_to_enter,
                        enter_direction=direction,
                        direction_streak=streak,
                    ),
                    additional_score,
                    additional_came_from,
                )
            )

        return immediate_neighbors


class UltraMap(Map):
    def get_next_node_data(
        self, node: Node
    ) -> list[tuple[Position, Direction, Streak]]:
        x, y = node.position

        accepted_positions = {
            Direction.UP: [(x, y - 4), 4],
            Direction.DOWN: [(x, y + 4), 4],
            Direction.RIGHT: [(x + 4, y), 4],
            Direction.LEFT: [(x - 4, y), 4],
        }

        if node.enter_direction:
            # Cannot move in the opposite direction
            accepted_positions.pop(node.enter_direction.opposite)

            # Update streak for node.enter_direction
            accepted_positions[node.enter_direction][1] = (
                node.direction_streak + 4
            )

            if node.direction_streak < 10:
                new_position = node.enter_direction.new_position(
                    node.position, diff=1
                )
                accepted_positions[node.enter_direction] = (
                    new_position,
                    node.direction_streak + 1,
                )
            elif node.direction_streak >= 10:
                accepted_positions.pop(node.enter_direction)

        return [
            (position, direction, streak)
            for direction, (position, streak) in accepted_positions.items()
            if self.is_valid_position(position)
        ]

    def build_additional_came_from(
        self, a: Position, b: Position, previous: Node, same_direction: bool
    ) -> tuple[dict[Node, Node], Optional[Node]]:
        positions = build_positions_list(a, b)

        streak = previous.direction_streak if same_direction else 0
        came_from = {}
        next = None
        for position in positions:
            streak += 1
            direction = Direction.from_two_points(
                start=previous.position, end=position
            )

            next = Node(
                position=position,
                distance_to_enter=self.get_distance_on(position),
                enter_direction=direction,
                direction_streak=streak,
            )
            came_from[next] = previous
            previous = next

        return came_from, next

    def get_neighbors(
        self, node: Node
    ) -> list[tuple[Node, int, dict[Node, Node]]]:
        immediate_neighbors = []

        for connected_position, direction, streak in self.get_next_node_data(
            node=node
        ):
            distance_to_enter = self.get_distance_on(connected_position)

            same_direction = node.enter_direction == direction

            additional_came_from, last_node = self.build_additional_came_from(
                a=node.position,
                b=connected_position,
                previous=node,
                same_direction=same_direction,
            )

            additional_score = 0
            for neighbor_node in additional_came_from:
                additional_score += neighbor_node.distance_to_enter

            neighbor = Node(
                position=connected_position,
                distance_to_enter=distance_to_enter,
                enter_direction=direction,
                direction_streak=streak,
            )

            if last_node:
                additional_came_from[neighbor] = last_node

            immediate_neighbors.append(
                (neighbor, additional_score, additional_came_from)
            )

        return immediate_neighbors


def build_positions_list(a: Position, b: Position) -> list[Position]:
    x_a, y_a = a
    x_b, y_b = b
    if x_a == x_b:
        if y_b < y_a:
            y_range = range(y_a - 1, y_b, -1)
        else:
            y_range = range(y_a + 1, y_b)
        return [(x_a, y) for y in y_range]
    elif y_a == y_b:
        if x_b < x_a:
            x_range = range(x_a - 1, x_b, -1)
        else:
            x_range = range(x_a + 1, x_b)
        return [(x, y_a) for x in x_range]
    else:
        raise RuntimeError("This is not an expected situation.")


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
