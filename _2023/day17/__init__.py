import math
from dataclasses import dataclass
from enum import Enum, auto

Position = tuple[int, int]
Distance = int
Tiles = list[list[Distance]]


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()

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


@dataclass
class Map:
    tiles: Tiles

    @property
    def max_x(self) -> int:
        return len(self.tiles[0]) - 1

    @property
    def max_y(self) -> int:
        return len(self.tiles) - 1

    @classmethod
    def from_data(cls, data: str) -> "Map":
        tiles = [
            [int(character) for character in line]
            for line in data.splitlines()
        ]
        return Map(tiles=tiles)

    def is_position_valid(self, position: Position) -> bool:
        x, y = position
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def get_distance_to_enter(self, position: Position) -> int:
        if not self.is_position_valid(position):
            raise RuntimeError(f"Position {position} is not valid")
        x, y = position
        return self.tiles[y][x]


@dataclass
class DijkstraResult:
    distances: dict[Position, int]
    shortest_previous_point: dict[Position, Position]


def get_point_to_visit_with_min_distance(
    points_to_visit: list[Position], distances: dict[Position, int]
) -> Position:
    point = None
    min_distance = math.inf
    for point_to_visit in points_to_visit:
        current_distance = distances[point_to_visit]
        if current_distance <= min_distance:
            point = point_to_visit
            min_distance = current_distance
    if not point:
        raise RuntimeError("No points to explore")
    return point


def get_last_directions(
    current_point: Position,
    shortest_previous_point: dict[Position, Position],
    amount: int = 2,
) -> list[Direction]:
    last_directions = []
    for i in range(amount):
        previous_point = shortest_previous_point[current_point]
        if previous_point:
            last_directions.append(
                Direction.from_two_points(
                    start=previous_point, end=current_point
                )
            )
            current_point = previous_point
    if len(last_directions) == amount:
        return last_directions
    else:
        return []


def get_neighbors(
    map: Map,
    shortest_previous_point: dict[Position, Position],
    points_to_visit: list[Position],
    position: Position,
) -> list[Position]:
    x, y = position

    two_last_directions = get_last_directions(
        current_point=position,
        shortest_previous_point=shortest_previous_point,
        amount=2,
    )

    neighbors = []
    for possible_position in [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]:
        # Skipping if position is not map
        if not map.is_position_valid(possible_position):
            continue

        # Skipping if position is already visited
        if possible_position not in points_to_visit:
            continue

        # Skipping according to puzzle constraint:
        # it can move at most three blocks in a single direction
        if two_last_directions:
            # If the existing path >= 2 moves
            directions = [
                *two_last_directions,
                Direction.from_two_points(
                    start=position, end=possible_position
                ),
            ]
            if all(d == directions[0] for d in directions):
                continue

        neighbors.append(possible_position)
    return neighbors


def dijkstra(map: Map, starting_point: Position):
    distances = {}
    shortest_previous_point = {}
    points_to_visit = []

    # Initiation phase
    for x in range(map.max_x + 1):
        for y in range(map.max_y + 1):
            position = (x, y)
            distances[position] = math.inf
            shortest_previous_point[position] = None
            points_to_visit.append(position)
    distances[starting_point] = 0

    # Construct shortest_previous_point mapping
    while points_to_visit:
        current_point = get_point_to_visit_with_min_distance(
            points_to_visit, distances
        )
        points_to_visit.remove(current_point)

        neighbors = get_neighbors(
            map=map,
            shortest_previous_point=shortest_previous_point,
            points_to_visit=points_to_visit,
            position=current_point,
        )

        for neighbor in neighbors:
            current_distance = distances[current_point]
            alternative_distance = (
                current_distance + map.get_distance_to_enter(neighbor)
            )
            if alternative_distance < distances[neighbor]:
                distances[neighbor] = alternative_distance
                shortest_previous_point[neighbor] = current_point

    return DijkstraResult(
        distances=distances,
        shortest_previous_point=shortest_previous_point,
    )
