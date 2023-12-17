from _2023.day17 import dijkstra, Map, a_star, Vertex
from _2023.load_input import load_input


def build_solution_tiles(map: Map, shortest_route: list[Vertex]):
    tiles = []
    for x in range(map.max_x + 1):
        tiles_line = []
        for y in range(map.max_y + 1):
            tiles_line.append(str(map.get_distance_on((x, y))))
        tiles.append(tiles_line)

    for vertex in shortest_route:
        x, y = vertex.end
        tiles[y][x] = vertex.direction.value

    return "\n".join(["".join(tiles_line) for tiles_line in tiles])


def _compute_solution(data: str) -> int:
    map = Map.from_data(data)
    dijkstra_result = dijkstra(map=map)
    return min(
        dijkstra_result.distances[end_vertex]
        for end_vertex in map.end_vertices
    )


def compute_solution(data: str) -> int:
    map = Map.from_data(data)
    path = a_star(map=map)
    return sum(vertex.distance for vertex in path)


if __name__ == "__main__":
    # < 1249
    print(compute_solution(load_input(17)))
