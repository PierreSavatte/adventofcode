import pytest

from _2023.day17 import Map, Direction, dijkstra
from _2023.day17.part1 import (
    compute_solution,
    rebuild_shortest_route,
    build_solution_tiles,
)


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


def test_map_can_be_loaded_from_input_file(get_data):
    map = Map.from_data(get_data("test_file_day17"))

    assert map.max_x == 12
    assert map.max_y == 12

    assert map.is_position_valid((25, 0)) is False
    assert map.is_position_valid((0, -1)) is False
    assert map.is_position_valid((0, 0)) is True

    assert map.get_distance_to_enter((0, 0)) == 2
    assert map.get_distance_to_enter((12, 12)) == 3
    assert map.get_distance_to_enter((12, 12)) == 3
    assert map.get_distance_to_enter((4, 5)) == 5


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


def test_shortest_path_can_be_computed(get_data):
    map = Map.from_data(get_data("test_file_day17"))
    starting_point = (0, 0)
    end_point = (map.max_x, map.max_y)
    dijkstra_result = dijkstra(map=map, starting_point=starting_point)

    shortest_route = rebuild_shortest_route(
        dijkstra_result.shortest_previous_point, starting_point, end_point
    )
    shortest_route.reverse()

    assert build_solution_tiles(map, shortest_route) == EXPECTED_SHORTEST_PATH


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day17")) == 102
