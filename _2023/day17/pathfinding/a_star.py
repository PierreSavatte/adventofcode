import math

from _2023.day17 import Vertex, Direction, Map
from _2023.day17.pathfinding import (
    get_vertex_to_visit_with_min_distance,
    ShortestRoute,
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
) -> ShortestRoute:
    vertices = []
    while current_vertex not in map.start_vertices:
        vertices.append(current_vertex)
        current_vertex = came_from[current_vertex]
    return ShortestRoute(vertices)


def a_star(map: Map) -> ShortestRoute:
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
            distances=f_score,
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

    raise RuntimeError("Was not able to find a path")
