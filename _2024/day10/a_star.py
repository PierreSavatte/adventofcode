import math
from typing import Callable

from _2024.day10 import MAP, POSITION

PATH = list[POSITION]


def reconstruct_path(
    came_from: dict[POSITION], current: POSITION
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


def a_star(
    map: MAP,
    get_neighbors: Callable,
    start_position: POSITION,
    end_position: POSITION,
) -> PATH:
    open_set = {start_position}
    came_from: dict[POSITION] = {}

    def get_f_score(position: POSITION) -> int:
        return euclidean_distance(position, end_position)

    g_score = {start_position: 0}
    f_score = {start_position: get_f_score(start_position)}

    while open_set:
        current = get_node_in_open_set_with_lowest_f_score(
            open_set=open_set, f_score=f_score
        )

        if current == end_position:
            return reconstruct_path(came_from, current)

        open_set.remove(current)

        neighbors = get_neighbors(map, current)
        for neighbor in neighbors:
            tentative_g_score = g_score[current]
            if tentative_g_score < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + get_f_score(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    raise RuntimeError("Was not able to find a path")
