import math
from typing import Optional

from tqdm import tqdm

from _2023.day17 import Node, Map, Position
from _2023.day17.pathfinding import get_neighbors, ShortestRoute


def get_end_node(
    shortest_previous_node: dict[Node, Optional[Node]],
    distances: dict[Node, int],
    end_position: Position,
) -> Node:
    node = None
    min_distance = math.inf
    for end_node in shortest_previous_node.keys():
        if end_node.position != end_position:
            continue

        distance = distances[end_node]
        if distance < min_distance:
            min_distance = distance
            node = end_node

    if node is None:
        raise RuntimeError("Didn't found the end node")

    return node


def reconstruct_path(
    map: Map,
    shortest_previous_node: dict[Node, Optional[Node]],
    distances: dict[Node, int],
) -> ShortestRoute:
    vertices = []
    current = get_end_node(
        shortest_previous_node=shortest_previous_node,
        distances=distances,
        end_position=map.end_position,
    )
    while current != map.start_node:
        vertices.append(current)
        current = shortest_previous_node[current]
    return ShortestRoute(vertices)


def get_node_to_visit_with_min_distance(
    nodes_to_visit: list[Node], distances: dict[Node, int]
) -> Node:
    node = None
    min_distance = math.inf
    for node_to_visit in nodes_to_visit:
        current_distance = distances[node_to_visit]
        if current_distance <= min_distance:
            node = node_to_visit
            min_distance = current_distance
    if not node:
        raise RuntimeError("No points to explore")
    return node


def dijkstra(map: Map) -> ShortestRoute:
    distances = {}
    shortest_previous_node = {}
    nodes_to_visit = []

    # Initiation phase
    for node in map.get_all_nodes():
        distances[node] = math.inf
        shortest_previous_node[node] = None
        nodes_to_visit.append(node)

    distances[map.start_node] = 0

    # Construct shortest_previous_point mapping
    progress_bar = tqdm(total=len(nodes_to_visit))
    while nodes_to_visit:
        current = get_node_to_visit_with_min_distance(
            nodes_to_visit, distances
        )
        nodes_to_visit.remove(current)

        neighbors = get_neighbors(map=map, current=current)
        for neighbor in neighbors:
            if neighbor not in nodes_to_visit:
                continue

            current_distance = distances[current]
            alternative_distance = (
                current_distance + neighbor.distance_to_enter
            )

            if alternative_distance < distances[neighbor]:
                distances[neighbor] = alternative_distance
                shortest_previous_node[neighbor] = current

        progress_bar.update(1)

    return reconstruct_path(
        map=map,
        distances=distances,
        shortest_previous_node=shortest_previous_node,
    )
