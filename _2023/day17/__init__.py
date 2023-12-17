import math
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from functools import cache, cached_property
from tqdm import tqdm
from collections import defaultdict

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

    @property
    def end_position(self) -> Position:
        return (self.max_x, self.max_y)

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
            if vertex.start == (0, 0):
                start_vertexes.append(vertex)
        return start_vertexes

    @cached_property
    def end_vertices(self) -> list[Vertex]:
        end_vertexes = []
        for vertex in self.vertices:
            if vertex.end == (self.max_x, self.max_y):
                end_vertexes.append(vertex)
        return end_vertexes

    @cache
    def get_neighbors(self, vertex: Vertex) -> list[Vertex]:
        neighbors = []
        for other_vertex in self.vertices:
            if other_vertex.start == vertex.end:
                neighbors.append(other_vertex)
        return neighbors

    def get_distance_on(self, position: Position):
        for vertex in self.vertices:
            if vertex.end == position:
                return vertex.distance

    def h(self, vertex: Vertex) -> float:
        x_a, y_a = vertex.start
        x_b, y_b = self.end_position
        # return math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
        return abs(x_b - x_a) + abs(y_b - y_a)


@dataclass
class DijkstraResult:
    distances: dict[Vertex, int]
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


def dijkstra(map: Map) -> DijkstraResult:
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
    progress_bar = tqdm(total=len(vertices_to_visit))
    while vertices_to_visit:
        current_vertex = get_vertex_to_visit_with_min_distance(
            vertices_to_visit, distances
        )
        vertices_to_visit.remove(current_vertex)
        progress_bar.update(1)

        neighbors = get_neighbors(
            map=map,
            shortest_previous_vertex=shortest_previous_vertex,
            vertices_to_visit=vertices_to_visit,
            vertex=current_vertex,
        )

        for neighbor in neighbors:
            current_distance = distances[current_vertex]
            alternative_distance = current_distance + neighbor.distance

            if alternative_distance < distances[neighbor]:
                distances[neighbor] = alternative_distance
                shortest_previous_vertex[neighbor] = current_vertex

                if neighbor in map.end_vertices:
                    return DijkstraResult(
                        distances=distances,
                        shortest_previous_vertex=shortest_previous_vertex,
                    )

    return DijkstraResult(
        distances=distances,
        shortest_previous_vertex=shortest_previous_vertex,
    )


def get_last_a_star_directions(
    came_from: dict[Vertex, Vertex],
    current_vertex: Vertex,
    amount: int,
) -> list[Direction]:
    directions = []
    for i in range(amount):
        directions.append(current_vertex.direction)
        if current_vertex not in came_from:
            return []
        current_vertex = came_from[current_vertex]
    return directions


def get_a_star_neighbors(
    map: Map,
    came_from: dict[Vertex, Vertex],
    vertex: Vertex,
) -> list[Vertex]:
    three_last_directions = get_last_a_star_directions(
        came_from=came_from, current_vertex=vertex, amount=3
    )
    if three_last_directions:
        same_last_three = all(
            d == three_last_directions[-1] for d in three_last_directions
        )
    else:
        same_last_three = False

    neighbors = []
    for potential_vertex in map.get_neighbors(vertex):
        # Skipping according to puzzle constraint:
        # it can move at most three blocks in a single direction
        if same_last_three:
            # If the existing path >= 3 moves
            additional_direction = potential_vertex.direction
            if additional_direction == three_last_directions[0]:
                continue

        neighbors.append(potential_vertex)
    return neighbors


def reconstruct_path(
    map: Map, came_from: dict[Vertex], current_vertex: Vertex
) -> list[Vertex]:
    vertices = []
    while current_vertex not in map.start_vertices:
        vertices.append(current_vertex)
        current_vertex = came_from[current_vertex]
    return vertices


def a_star(map: Map) -> list[Vertex]:
    open_set = [start_vertex for start_vertex in map.start_vertices]
    came_from = {}

    g_score = {}
    f_score = {}
    for vertex in map.vertices:
        g_score[vertex] = math.inf
        f_score[vertex] = math.inf

    for start_vertex in map.start_vertices:
        g_score[start_vertex] = 0
        f_score[start_vertex] = map.h(start_vertex)

    while open_set:
        current_vertex = get_vertex_to_visit_with_min_distance(
            vertices_to_visit=open_set,
            distances=dict(f_score),
        )
        if current_vertex in map.end_vertices:
            return reconstruct_path(
                map=map, came_from=came_from, current_vertex=current_vertex
            )

        open_set.remove(current_vertex)
        for neighbor in get_a_star_neighbors(
            map=map, came_from=came_from, vertex=current_vertex
        ):
            tentative_g_score = g_score[current_vertex] + neighbor.distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_vertex
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + map.h(neighbor)
                if neighbor not in open_set:
                    open_set.append(neighbor)
