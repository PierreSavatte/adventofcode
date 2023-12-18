import math
from dataclasses import dataclass
from typing import Optional

from tqdm import tqdm

from _2023.day17 import Vertex, Direction, Map
from _2023.day17.pathfinding import (
    get_vertex_to_visit_with_min_distance,
    ShortestRoute,
)


@dataclass
class DijkstraResult:
    distances: dict[Vertex, int]
    shortest_previous_vertex: dict[Vertex, Vertex]


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


def reconstruct_path(
    map: Map,
    shortest_previous_vertex: dict[Vertex, Optional[Vertex]],
    distances: dict[Vertex, int],
) -> ShortestRoute:
    end_vertex = None
    min_distance = math.inf
    for vertex in map.end_vertices:
        if distances[vertex] < min_distance:
            end_vertex = vertex

    vertices = []
    current_vertex = end_vertex
    while current_vertex not in map.start_vertices:
        vertices.append(current_vertex)
        current_vertex = shortest_previous_vertex[current_vertex]
    return ShortestRoute(vertices)


def dijkstra(map: Map) -> ShortestRoute:
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
                    return reconstruct_path(
                        map=map,
                        distances=distances,
                        shortest_previous_vertex=shortest_previous_vertex,
                    )

    return reconstruct_path(
        map=map,
        distances=distances,
        shortest_previous_vertex=shortest_previous_vertex,
    )
