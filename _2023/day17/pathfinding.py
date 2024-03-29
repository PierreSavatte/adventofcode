import math

from tqdm import tqdm

from _2023.day17 import Map, Node
from _2023.day17 import build_solution_tiles


def reconstruct_path(came_from: dict[Node], current: Node) -> list[Node]:
    total_path = [current]
    current = came_from[current]
    while current in came_from:
        total_path.insert(0, current)
        current = came_from[current]
    return total_path


def get_node_in_open_set_with_lowest_f_score(
    open_set: set[Node], f_score: dict[Node, int]
) -> Node:
    min_score = math.inf
    min_node = None
    for node in open_set:
        score = f_score[node]
        if score < min_score:
            min_score = score
            min_node = node
    return min_node


def display_best_path(map: Map, came_from: dict[Node], current: Node):
    if not came_from:
        return
    shortest_route = reconstruct_path(came_from, current)
    tiles = build_solution_tiles(
        map=map, shortest_route=shortest_route, colorized=True
    )
    print()
    print(f"{current=}")
    print(tiles)


def a_star(map: Map, display_progress_bar: bool = False) -> list[Node]:
    open_set = {map.start_node}
    came_from = {}

    g_score = {map.start_node: 0}
    f_score = {map.start_node: map.h(map.start_node)}

    progress_bar = tqdm(
        total=map.max_x + map.max_y, disable=not display_progress_bar
    )
    progress = 0
    while open_set:
        current = get_node_in_open_set_with_lowest_f_score(
            open_set=open_set, f_score=f_score
        )

        current_progress = sum(current.position)
        if current_progress > progress:
            progress_bar.update(current_progress - progress)
            progress = current_progress

        if current.position == map.end_position:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        for (
            neighbor,
            additional_score,
            additional_came_from,
        ) in map.get_neighbors(current):
            tentative_g_score = (
                g_score[current]
                + additional_score
                + neighbor.distance_to_enter
            )
            if tentative_g_score < g_score.get(neighbor, math.inf):
                if additional_came_from:
                    came_from.update(additional_came_from)
                else:
                    came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + map.h(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    raise RuntimeError("Was not able to find a path")
