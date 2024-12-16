import math
from enum import Enum
from typing import Any, Optional, Protocol

POSITION = tuple[int, int]
PATH = list[POSITION]


class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

    def to_str(self) -> str:
        map = {
            Direction.UP: "^",
            Direction.LEFT: "<",
            Direction.DOWN: "v",
            Direction.RIGHT: ">",
        }
        return map[self]

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


def reconstruct_path(
    came_from: dict[POSITION, POSITION], current: POSITION
) -> list[POSITION]:
    total_path = [current]
    current = came_from[current]
    while current in came_from:
        total_path.insert(0, current)
        current = came_from[current]
    return total_path


def get_node_in_open_set_with_lowest_f_score(
    open_set: set[POSITION], f_score: dict[POSITION, int]
) -> POSITION:
    min_score = math.inf
    min_node = None
    for node in open_set:
        score = f_score[node]
        if score < min_score:
            min_score = score
            min_node = node
    return min_node


def euclidean_distance(a: POSITION, b: POSITION) -> int:
    x_a, y_a = a
    x_b, y_b = b
    return abs(x_b - x_a) + abs(y_b - y_a)


def get_f_score(position: POSITION, end_position: POSITION) -> int:
    return euclidean_distance(position, end_position)


class GetFScore(Protocol):
    def __call__(self, position: POSITION, end_position: POSITION) -> int:
        raise NotImplementedError()


class GetNeighbors(Protocol):
    def __call__(
        self, map: Any, current: POSITION, direction: Direction
    ) -> list[POSITION]:
        raise NotImplementedError()


class GetDistance(Protocol):
    def __call__(
        self,
        current: POSITION,
        current_direction: Direction,
        neighbor: POSITION,
    ) -> int:
        raise NotImplementedError()


def a_star(
    map: Any,
    get_neighbors: GetNeighbors,
    start_position: POSITION,
    end_position: POSITION,
    distance_function: GetDistance,
    f_function: GetFScore = get_f_score,
) -> PATH:
    open_set = {start_position}
    came_from: dict[POSITION, POSITION] = {}

    g_score = {start_position: 0}
    f_score = {
        start_position: f_function(
            position=start_position, end_position=end_position
        )
    }

    while open_set:
        current = get_node_in_open_set_with_lowest_f_score(
            open_set=open_set, f_score=f_score
        )
        previous = came_from.get(current)
        direction = Direction.from_two_points(previous, current)

        if current == end_position:
            return [start_position, *reconstruct_path(came_from, current)]

        open_set.remove(current)

        neighbors = get_neighbors(
            map=map, current=current, direction=direction
        )
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + distance_function(
                current=current, current_direction=direction, neighbor=neighbor
            )
            if tentative_g_score < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + f_function(
                    position=neighbor, end_position=end_position
                )
                if neighbor not in open_set:
                    open_set.add(neighbor)

    raise RuntimeError("Was not able to find a path")
