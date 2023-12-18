import pytest

from _2023.day17 import Map, Direction, is_position_valid, Vertex
from _2023.day17.part1 import compute_solution, build_solution_tiles
from _2023.day17.pathfinding.a_star import a_star
from _2023.day17.pathfinding.dijkstra import dijkstra

EXPECTED_SHORTEST_PATH = """2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>"""


def test_validity_of_position_can_be_computed():
    max_x = 12
    max_y = 12

    assert (
        is_position_valid(max_x=max_x, max_y=max_y, position=(25, 0)) is False
    )
    assert (
        is_position_valid(max_x=max_x, max_y=max_y, position=(0, -1)) is False
    )
    assert is_position_valid(max_x=max_x, max_y=max_y, position=(0, 0)) is True


def test_map_can_be_loaded_from_input_file(get_data):
    map = Map.from_data(get_data("test_file_day17"))

    assert map.max_x == 12
    assert map.max_y == 12

    assert map.start_vertices == [
        Vertex(start=(0, 0), end=(1, 0), distance=4),
        Vertex(start=(0, 0), end=(0, 1), distance=3),
    ]
    assert map.end_vertices == [
        Vertex(start=(11, 12), end=(12, 12), distance=3),
        Vertex(start=(12, 11), end=(12, 12), distance=3),
    ]


@pytest.mark.parametrize(
    "start, end, expected_direction",
    [
        ((1, 1), (2, 1), Direction.RIGHT),
        ((1, 1), (1, 2), Direction.DOWN),
        ((1, 1), (0, 1), Direction.LEFT),
        ((1, 1), (1, 0), Direction.UP),
    ],
)
def test_direction_can_be_computed_from_two_points(
    start, end, expected_direction
):
    assert (
        Direction.from_two_points(start=start, end=end) == expected_direction
    )


@pytest.mark.parametrize("algorithm", [a_star, dijkstra])
def test_shortest_path_can_be_computed(get_data, algorithm):
    map = Map.from_data(get_data("test_file_day17"))
    shortest_route = algorithm(map=map)

    assert build_solution_tiles(map, shortest_route) == EXPECTED_SHORTEST_PATH


@pytest.mark.parametrize("algorithm", [a_star, dijkstra])
def test_solution_can_be_computed(get_data, algorithm):
    assert (
        compute_solution(get_data("test_file_day17"), algorithm=algorithm)
        == 102
    )
