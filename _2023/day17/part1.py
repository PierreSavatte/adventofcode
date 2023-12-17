from _2023.day17 import dijkstra, Map
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    map = Map.from_data(data)
    starting_point = (0, 0)
    end_point = (map.max_x, map.max_y)
    dijkstra_result = dijkstra(map=map, starting_point=starting_point)
    return dijkstra_result.distances[end_point]


if __name__ == "__main__":
    print(compute_solution(load_input(17)))
