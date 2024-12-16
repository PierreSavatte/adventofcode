import pytest
from _2024.day16 import (
    Direction,
    Map,
    compute_distance,
    compute_total_distance,
    parse_input,
)

TEST_INPUT = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
SECOND_TEST_INPUT = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

MAP = Map(
    map=[
        "###############",
        "#.......#.....#",
        "#.#.###.#.###.#",
        "#.....#.#...#.#",
        "#.###.#####.#.#",
        "#.#.#.......#.#",
        "#.#.#####.###.#",
        "#...........#.#",
        "###.#.#####.#.#",
        "#...#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.....#...#.#.#",
        "#.###.#.#.#.#.#",
        "#...#.....#...#",
        "###############",
    ],
    start=(1, 13),
    end=(13, 1),
)
SECOND_MAP = Map(
    map=[
        "#################",
        "#...#...#...#...#",
        "#.#.#.#.#.#.#.#.#",
        "#.#.#.#...#...#.#",
        "#.#.#.#.###.#.#.#",
        "#...#.#.#.....#.#",
        "#.#.#.#.#.#####.#",
        "#.#...#.#.#.....#",
        "#.#.#####.#.###.#",
        "#.#.#.......#...#",
        "#.#.###.#####.###",
        "#.#.#...#.....#.#",
        "#.#.#.#####.###.#",
        "#.#.#.........#.#",
        "#.#.#.#########.#",
        "#.#.............#",
        "#################",
    ],
    start=(1, 15),
    end=(15, 1),
)


@pytest.mark.parametrize(
    "one, another, nb_90_rotation",
    [
        # Same direction
        (Direction.UP, Direction.UP, 0),
        (Direction.DOWN, Direction.DOWN, 0),
        (Direction.LEFT, Direction.LEFT, 0),
        (Direction.RIGHT, Direction.RIGHT, 0),
        # One rotation
        (Direction.UP, Direction.RIGHT, 1),
        (Direction.UP, Direction.LEFT, 1),
        (Direction.DOWN, Direction.RIGHT, 1),
        (Direction.DOWN, Direction.LEFT, 1),
        # Two rotations
        (Direction.UP, Direction.DOWN, 2),
        (Direction.RIGHT, Direction.LEFT, 2),
    ],
)
def test_direction_can_compute_the_number_of_90_rotation_with_another(
    one, another, nb_90_rotation
):
    assert one.get_nb_90_rotation(another) == nb_90_rotation
    assert another.get_nb_90_rotation(one) == nb_90_rotation


@pytest.mark.parametrize(
    "input, map",
    [
        (TEST_INPUT, MAP),
        (SECOND_TEST_INPUT, SECOND_MAP),
    ],
)
def test_input_can_be_parsed(input, map):
    assert parse_input(input) == map


@pytest.mark.parametrize(
    "current, current_direction, neighbor, expected_distance",
    [
        ((13, 2), Direction.UP, (13, 1), 1),
        ((1, 13), Direction.RIGHT, (1, 12), 1001),
        ((1, 13), Direction.RIGHT, (2, 13), 1),
    ],
)
def test_distance_between_two_points_can_be_computed(
    current, current_direction, neighbor, expected_distance
):
    assert (
        compute_distance(current, current_direction, neighbor)
        == expected_distance
    )


@pytest.mark.parametrize(
    "map, path_displayed, expected_path",
    [
        (
            SECOND_MAP,
            """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################""",
            [
                (1, 15),
                (1, 14),
                (1, 13),
                (1, 12),
                (1, 11),
                (1, 10),
                (1, 9),
                (1, 8),
                (1, 7),
                (1, 6),
                (1, 5),
                (2, 5),
                (3, 5),
                (3, 6),
                (3, 7),
                (3, 8),
                (3, 9),
                (3, 10),
                (3, 11),
                (3, 12),
                (3, 13),
                (3, 14),
                (3, 15),
                (4, 15),
                (5, 15),
                (5, 14),
                (5, 13),
                (5, 12),
                (5, 11),
                (6, 11),
                (7, 11),
                (7, 10),
                (7, 9),
                (8, 9),
                (9, 9),
                (10, 9),
                (11, 9),
                (11, 8),
                (11, 7),
                (12, 7),
                (13, 7),
                (14, 7),
                (15, 7),
                (15, 6),
                (15, 5),
                (15, 4),
                (15, 3),
                (15, 2),
                (15, 1),
            ],
        ),
    ],
)
def test_optimal_path_can_be_computed(map, path_displayed, expected_path):
    path = map.get_optimal_path()

    assert map.plot_path_in_map(path) == path_displayed

    assert path == expected_path


@pytest.mark.parametrize(
    "map, distance",
    [
        (MAP, 7036),
        (SECOND_MAP, 11048),
    ],
)
def test_total_distance_can_be_computed(map, distance):
    path = map.get_optimal_path()
    assert compute_total_distance(path) == distance
