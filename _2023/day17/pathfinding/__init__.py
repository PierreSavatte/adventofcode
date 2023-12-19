import math

from _2023.day17 import Node


def get_vertex_to_visit_with_min_distance(
    vertices_to_visit: list[Node], distances: dict[Node, int]
) -> Node:
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


class ShortestRoute(list[Node]):
    ...
