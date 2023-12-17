from copy import deepcopy

from _2023.day17 import dijkstra, Map, Position, Direction
from _2023.load_input import load_input


def rebuild_shortest_route(
    shortest_previous_point: dict[Position, Position],
    starting_point: Position,
    end_point: Position,
) -> list[tuple[Position, Direction]]:
    shortest_route = []
    current_point = end_point
    while current_point != starting_point:
        previous_point = shortest_previous_point[current_point]

        shortest_route.append(
            (
                current_point,
                Direction.from_two_points(previous_point, current_point),
            )
        )

        current_point = previous_point
    return shortest_route


def build_solution_tiles(
    map: Map, shortest_route: list[tuple[Position, Direction]]
):
    tiles = deepcopy(map.tiles)
    for position, direction in shortest_route:
        x, y = position
        tiles[y][x] = direction.value

    data = "\n".join(["".join([str(char) for char in line]) for line in tiles])

    return data


def compute_solution(data: str) -> int:
    map = Map.from_data(data)
    starting_point = (0, 0)
    end_point = (map.max_x, map.max_y)
    dijkstra_result = dijkstra(map=map, starting_point=starting_point)
    return dijkstra_result.distances[end_point]


if __name__ == "__main__":
    print(compute_solution(load_input(17)))
