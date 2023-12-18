import cProfile
import pstats
from typing import Optional, Callable

from _2023.day17 import Map, Vertex, Direction
from _2023.day17.pathfinding.dijkstra import dijkstra
from _2023.day17.pathfinding.a_star import a_star
from _2023.load_input import load_input


def build_solution_tiles(map: Map, shortest_route: list[Vertex]):
    tiles = []
    for y in range(map.max_x + 1):
        tiles_line = []
        for x in range(map.max_y + 1):
            tiles_line.append(str(map.get_distance_on((x, y))))
        tiles.append(tiles_line)

    first_vertex = shortest_route[-1]
    first_tile = map.start_position
    second_tile = first_vertex.start
    direction = Direction.from_two_points(start=first_tile, end=second_tile)
    tiles[second_tile[1]][second_tile[0]] = direction.value

    for vertex in shortest_route:
        x, y = vertex.end
        tiles[y][x] = vertex.direction.value

    return "\n".join(["".join(tiles_line) for tiles_line in tiles])


def compute_solution(data: str, algorithm: Optional[Callable] = None) -> int:
    if algorithm is None:
        algorithm = a_star
    map = Map.from_data(data)
    path = algorithm(map=map)
    return sum(vertex.distance for vertex in path)


def profiling():
    data = load_input(17)
    with cProfile.Profile() as pr:
        try:
            compute_solution(data, algorithm=dijkstra)
        except KeyboardInterrupt:
            ...
        finally:
            pr.dump_stats("profiling")

    stats = pstats.Stats("profiling")
    stats.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(15)


if __name__ == "__main__":
    # < 1249
    print(compute_solution(load_input(17)))
