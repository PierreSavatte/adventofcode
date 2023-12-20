import pytest

from _2023.day17 import Map, Direction, Node
from _2023.day17.part1 import compute_solution

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


def test_validity_of_position_can_be_computed(get_data):
    map = Map.from_data(get_data("test_file_day17"))
    assert map.max_x == 12
    assert map.max_y == 12

    assert map.is_valid_position(position=(25, 0)) is False
    assert map.is_valid_position(position=(0, -1)) is False
    assert map.is_valid_position(position=(0, 0)) is True


def test_map_can_be_loaded_from_input_file(get_data):
    map = Map.from_data(get_data("test_file_day17"))

    assert map.max_x == 12
    assert map.max_y == 12

    assert map.start_position == (0, 0)
    assert map.end_position == (12, 12)


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


@pytest.mark.parametrize(
    "input_node, expected_neighbors",
    [
        (
            Node(
                position=(3, 3),
                distance_to_enter=6,
                enter_direction=Direction.DOWN,
                direction_streak=2,
            ),
            [
                Node(
                    position=(4, 3),
                    distance_to_enter=5,
                    enter_direction=Direction.RIGHT,
                    direction_streak=1,
                ),
                Node(
                    position=(3, 4),
                    distance_to_enter=6,
                    enter_direction=Direction.DOWN,
                    direction_streak=3,
                ),
                Node(
                    position=(2, 3),
                    distance_to_enter=4,
                    enter_direction=Direction.LEFT,
                    direction_streak=1,
                ),
            ],
        ),
        (
            Node(
                position=(3, 3),
                distance_to_enter=6,
                enter_direction=Direction.RIGHT,
                direction_streak=2,
            ),
            [
                Node(
                    position=(4, 3),
                    distance_to_enter=5,
                    enter_direction=Direction.RIGHT,
                    direction_streak=3,
                ),
                Node(
                    position=(3, 4),
                    distance_to_enter=6,
                    enter_direction=Direction.DOWN,
                    direction_streak=1,
                ),
                Node(
                    position=(3, 2),
                    distance_to_enter=5,
                    enter_direction=Direction.UP,
                    direction_streak=1,
                ),
            ],
        ),
    ],
)
def test_map_can_give_immediate_neighbors(
    get_data, input_node, expected_neighbors
):
    map = Map.from_data(get_data("test_file_day17"))

    assert map.get_immediate_neighbors(input_node) == expected_neighbors


def test_map_can_build_its_node_set(get_data):
    map = Map.from_data(get_data("test_file_day17"))

    all_nodes = list(map.get_all_nodes())

    assert len(all_nodes) == 1717


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day17")) == 102
