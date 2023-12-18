from dataclasses import dataclass
from enum import Enum
from functools import cache, cached_property

Position = tuple[int, int]
Distance = int
Tiles = list[list[Distance]]


@cache
def is_position_valid(position: Position, max_x: int, max_y: int) -> bool:
    x, y = position
    return 0 <= x <= max_x and 0 <= y <= max_y


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    RIGHT = ">"
    LEFT = "<"

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
class Vertex:
    start: Position
    end: Position
    distance: int

    @property
    def direction(self) -> Direction:
        return Direction.from_two_points(start=self.start, end=self.end)

    def __hash__(self):
        return hash((self.start, self.end, self.distance))


@dataclass
class Map:
    vertices: list[Vertex]

    max_x: int
    max_y: int

    @cached_property
    def start_position(self) -> Position:
        return 0, 0

    @cached_property
    def end_position(self) -> Position:
        return self.max_x, self.max_y

    def __hash__(self):
        return hash(tuple(self.vertices))

    @classmethod
    def from_data(cls, data: str) -> "Map":
        lines = data.splitlines()
        max_y = len(lines) - 1
        max_x = len(lines[0]) - 1

        vertices = []
        for y, line in enumerate(data.splitlines()):
            for x, character in enumerate(line):
                current_position = (x, y)
                distance = int(character)
                for connected_position in [
                    (x + 1, y),
                    (x - 1, y),
                    (x, y + 1),
                    (x, y - 1),
                ]:
                    if is_position_valid(
                        position=connected_position, max_x=max_x, max_y=max_y
                    ):
                        vertices.append(
                            Vertex(
                                start=connected_position,
                                end=current_position,
                                distance=distance,
                            )
                        )

        return Map(
            max_x=max_x,
            max_y=max_y,
            vertices=vertices,
        )

    @cached_property
    def start_vertices(self) -> list[Vertex]:
        start_vertexes = []
        for vertex in self.vertices:
            if vertex.start == self.start_position:
                start_vertexes.append(vertex)
        return start_vertexes

    @cached_property
    def end_vertices(self) -> list[Vertex]:
        end_vertexes = []
        for vertex in self.vertices:
            if vertex.end == self.end_position:
                end_vertexes.append(vertex)
        return end_vertexes

    @cache
    def get_neighbors(self, vertex: Vertex) -> list[Vertex]:
        neighbors = []
        for other_vertex in self.vertices:
            if other_vertex.start == vertex.end:
                neighbors.append(other_vertex)
        return neighbors

    @cache
    def get_distance_on(self, position: Position):
        for vertex in self.vertices:
            if vertex.end == position:
                return vertex.distance

    @cache
    def h(self, vertex: Vertex) -> float:
        x_a, y_a = vertex.start
        x_b, y_b = self.end_position
        return abs(x_b - x_a) + abs(y_b - y_a)
