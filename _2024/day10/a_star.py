import math
from enum import Enum
from queue import PriorityQueue
from typing import Any, Optional, Protocol, Union

POSITION = tuple[int, int]
PATH = list[POSITION]


class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

    def opposite(self) -> "Direction":
        mapping = {
            Direction.UP: Direction.DOWN,
            Direction.LEFT: Direction.RIGHT,
            Direction.DOWN: Direction.UP,
            Direction.RIGHT: Direction.LEFT,
        }
        return mapping[self]

    def to_str(self) -> str:
        mapping = {
            Direction.UP: "^",
            Direction.LEFT: "<",
            Direction.DOWN: "v",
            Direction.RIGHT: ">",
        }
        return mapping[self]

    @classmethod
    def from_two_points(
        cls, previous: Optional[POSITION], current: POSITION
    ) -> "Direction":
        if previous is None:
            return Direction.RIGHT

        x_previous, y_previous = previous
        x_current, y_current = current

        if x_previous == x_current:
            if y_previous > y_current:
                return cls.UP
            else:
                return cls.DOWN
        else:
            if x_previous > x_current:
                return cls.LEFT
            else:
                return cls.RIGHT

    def get_nb_90_rotation(self, other: "Direction") -> int:
        if abs(self.value - other.value) // 3 == 1:
            return 1
        return abs(self.value - other.value)

    def to_delta_position(self):
        delta_position_mapping = {
            Direction.UP: (0, -1),
            Direction.DOWN: (0, 1),
            Direction.LEFT: (-1, 0),
            Direction.RIGHT: (1, 0),
        }
        return delta_position_mapping[self]

    def __lt__(self, other: "Direction") -> bool:
        return self.to_delta_position() <= other.to_delta_position()


def euclidean_distance(
    current: POSITION,
    neighbor: POSITION,
    current_direction: Optional[Direction] = None,
) -> int:
    x_a, y_a = current
    x_b, y_b = neighbor
    return abs(x_b - x_a) + abs(y_b - y_a)


class GetNeighbors(Protocol):
    def __call__(
        self, map: Any, current: POSITION, direction: Direction
    ) -> list[POSITION]:
        raise NotImplementedError()


class GetDistance(Protocol):
    def __call__(
        self,
        current: POSITION,
        neighbor: POSITION,
        current_direction: Optional[Direction] = None,
    ) -> int:
        raise NotImplementedError()


def a_star(
    map: Any,
    get_neighbors: GetNeighbors,
    start_position: POSITION,
    end_position: POSITION,
    distance_function: GetDistance,
    multiple_optimal_paths: bool = False,
) -> Union[PATH, list[PATH]]:
    open_set = PriorityQueue()
    open_set.put(item=(0, start_position, Direction.RIGHT, [start_position]))

    g_score = {(start_position, Direction.RIGHT): 0}
    paths = []
    optimal_distance = None

    while not open_set.empty():
        distance, current, direction, path = open_set.get()

        if current == end_position:
            if multiple_optimal_paths:
                if optimal_distance is None:
                    optimal_distance = distance
                if distance == optimal_distance:
                    paths.append(path)
            else:
                return path

        neighbors = get_neighbors(
            map=map, current=current, direction=direction
        )
        for neighbor in neighbors:
            next_direction = Direction.from_two_points(current, neighbor)
            distance_current_neighbor = distance_function(
                current=current, current_direction=direction, neighbor=neighbor
            )
            tentative_g_score = distance + distance_current_neighbor

            already_existing_g_score = g_score.get(
                (neighbor, next_direction), math.inf
            )
            if tentative_g_score <= already_existing_g_score:
                g_score[(neighbor, next_direction)] = tentative_g_score
                open_set.put(
                    item=(
                        tentative_g_score,
                        neighbor,
                        next_direction,
                        [*path, neighbor],
                    )
                )
    if multiple_optimal_paths:
        return paths
    else:
        raise RuntimeError("Was not able to find a path")
