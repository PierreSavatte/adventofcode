import math
from dataclasses import dataclass
from enum import Enum
from typing import Optional

Position = tuple[int, int]
Distance = int
Tiles = list[list[Distance]]


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

    @property
    def start_vertices(self) -> list[Vertex]:
        start_vertexes = []
        for vertex in self.vertices:
            if vertex.start == (0, 0):
                start_vertexes.append(vertex)
        return start_vertexes

    @property
    def end_vertices(self) -> list[Vertex]:
        end_vertexes = []
        for vertex in self.vertices:
            if vertex.end == (self.max_x, self.max_y):
                end_vertexes.append(vertex)
        return end_vertexes

    def get_neighbors(self, vertex: Vertex) -> list[Vertex]:
        neighbors = []
        for other_vertex in self.vertices:
            if other_vertex.start == vertex.end:
                neighbors.append(other_vertex)
        return neighbors


@dataclass
class DijkstraResult:
    distances: dict[Position, int]
    shortest_previous_vertex: dict[Vertex, Vertex]


def get_vertex_to_visit_with_min_distance(
    vertices_to_visit: list[Vertex], distances: dict[Vertex, int]
) -> Vertex:
    vertex = None
    min_distance = math.inf
    for vertex_to_visit in vertices_to_visit:
        current_distance = distances[vertex_to_visit]
        if current_distance <= min_distance:
            vertex = vertex_to_visit
            min_distance = current_distance
    if not vertex:
        raise RuntimeError("No points to explore")
    return vertex


def get_last_directions(
    current_vertex: Vertex,
    shortest_previous_vertex: dict[Vertex, Optional[Vertex]],
    amount: int = 2,
) -> list[Direction]:
    last_directions = []
    for i in range(amount):
        last_directions.append(current_vertex.direction)
        current_vertex = shortest_previous_vertex[current_vertex]
        if not current_vertex:
            break
    if len(last_directions) == amount:
        return last_directions
    else:
        return []


def get_neighbors(
    map: Map,
    shortest_previous_vertex: dict[Vertex, Optional[Vertex]],
    vertices_to_visit: list[Vertex],
    vertex: Vertex,
) -> list[Vertex]:
    three_last_directions = get_last_directions(
        current_vertex=vertex,
        shortest_previous_vertex=shortest_previous_vertex,
        amount=3,
    )
    if three_last_directions:
        same_last_three = all(
            d == three_last_directions[-1] for d in three_last_directions
        )
    else:
        same_last_three = False

    neighbors = []
    for potential_vertex in map.get_neighbors(vertex):
        # Skipping if position is already visited
        if potential_vertex not in vertices_to_visit:
            continue

        # Skipping according to puzzle constraint:
        # it can move at most three blocks in a single direction
        if same_last_three:
            # If the existing path >= 3 moves
            additional_direction = potential_vertex.direction
            if additional_direction == three_last_directions[0]:
                continue

        neighbors.append(potential_vertex)
    return neighbors


def dijkstra(map: Map):
    distances = {}
    shortest_previous_vertex = {}
    vertices_to_visit = []

    # Initiation phase
    for vertex in map.vertices:
        distances[vertex] = math.inf
        shortest_previous_vertex[vertex] = None
        vertices_to_visit.append(vertex)

    for start_vertex in map.start_vertices:
        distances[start_vertex] = 0

    # Construct shortest_previous_point mapping
    while vertices_to_visit:
        current_vertex = get_vertex_to_visit_with_min_distance(
            vertices_to_visit, distances
        )
        vertices_to_visit.remove(current_vertex)

        neighbors = get_neighbors(
            map=map,
            shortest_previous_vertex=shortest_previous_vertex,
            vertices_to_visit=vertices_to_visit,
            vertex=current_vertex,
        )

        # print(f"Visiting {current_point}: {neighbors=}")

        for neighbor in neighbors:
            current_distance = distances[current_vertex]
            alternative_distance = current_distance + neighbor.distance

            # if neighbor == (4, 0):
            #     print(
            #         f"For point {neighbor}: {alternative_distance=}, "
            #         f"existing={distances[neighbor]}"
            #     )

            if alternative_distance < distances[neighbor]:
                distances[neighbor] = alternative_distance
                shortest_previous_vertex[neighbor] = current_vertex

    return DijkstraResult(
        distances=distances,
        shortest_previous_vertex=shortest_previous_vertex,
    )
