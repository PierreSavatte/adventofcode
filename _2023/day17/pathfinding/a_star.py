import math

from _2023.day17 import Node, Map
from _2023.day17.pathfinding import ShortestRoute, get_neighbors


def reconstruct_path(came_from: dict[Node], current: Node) -> ShortestRoute:
    total_path = [current]
    while current in came_from:
        current = came_from[current]

        total_path.insert(0, current)
    return ShortestRoute(total_path)


def get_node_in_open_set_with_lowers_f_score(
    open_set: list[Node], f_score: dict[Node, int]
) -> Node:
    min_node = None
    min_distance = math.inf
    for node in open_set:
        current_distance = f_score.get(node, math.inf)
        if current_distance <= min_distance:
            min_node = node
            min_distance = current_distance
    if not min_node:
        raise RuntimeError("No points to explore")
    return min_node


def a_star(map: Map) -> ShortestRoute:
    open_set = [map.start_node]
    came_from = {}

    g_score = {map.start_node: 0}
    f_score = {map.start_node: map.h(map.start_node)}

    while open_set:
        current = get_node_in_open_set_with_lowers_f_score(
            open_set=open_set, f_score=f_score
        )
        if current == map.end_node:
            return reconstruct_path(came_from=came_from, current=current)

        open_set.remove(current)
        for neighbor in get_neighbors(map=map, current=current):
            tentative_g_score = g_score[current] + neighbor.distance_to_enter
            if tentative_g_score < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + map.h(neighbor)
                if neighbor not in open_set:
                    open_set.append(neighbor)

    raise RuntimeError("Was not able to find a path")
