from _2023.day17 import dijkstra, Map
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    map = Map.from_data(data)
    dijkstra_result = dijkstra(map=map)
    return min(
        dijkstra_result.distances[end_vertex]
        for end_vertex in map.end_vertices
    )


if __name__ == "__main__":
    print(compute_solution(load_input(17)))
