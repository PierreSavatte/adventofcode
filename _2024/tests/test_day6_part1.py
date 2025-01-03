import pytest
from _2024.day6 import Direction, Line, Map, parse_input
from _2024.day6.part1 import compute_solution

TEST_INPUT = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

MAP = Map(
    size=10,
    guard_starting_position=(4, 6),
    obstacles=[
        (4, 0),
        (9, 1),
        (2, 3),
        (7, 4),
        (1, 6),
        (8, 7),
        (0, 8),
        (6, 9),
    ],
)


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == MAP


@pytest.mark.parametrize(
    "start, end, expected_positions",
    [
        ((0, 0), (0, 0), {(0, 0)}),
        ((0, 0), (3, 0), {(0, 0), (1, 0), (2, 0), (3, 0)}),
        ((3, 0), (0, 0), {(0, 0), (1, 0), (2, 0), (3, 0)}),
        ((0, 3), (0, 0), {(0, 0), (0, 1), (0, 2), (0, 3)}),
        ((0, 0), (0, 3), {(0, 0), (0, 1), (0, 2), (0, 3)}),
    ],
)
def test_positions_can_be_computed_in_a_line(start, end, expected_positions):
    assert (
        Line(start, end, Direction.UP).compute_positions()
        == expected_positions
    )


@pytest.mark.parametrize("start, end", [((0, 0), (1, 1)), ((1, 1), (0, 0))])
def test_error_is_raised_when_positions_are_not_in_a_line(start, end):
    line = Line(start, end, Direction.UP)
    with pytest.raises(ValueError):
        line.compute_positions()


@pytest.mark.parametrize(
    "direction, expected_new_direction",
    [
        (Direction.UP, Direction.RIGHT),
        (Direction.RIGHT, Direction.DOWN),
        (Direction.DOWN, Direction.LEFT),
        (Direction.LEFT, Direction.UP),
    ],
)
def test_direction_can_turn_90_degrees(direction, expected_new_direction):
    assert direction.turn_90_degrees() == expected_new_direction


@pytest.mark.parametrize(
    "position, direction, expected_new_position",
    [
        ((1, 1), Direction.UP, (1, 2)),
        ((1, 1), Direction.RIGHT, (0, 1)),
        ((1, 1), Direction.DOWN, (1, 0)),
        ((1, 1), Direction.LEFT, (2, 1)),
    ],
)
def test_direction_can_return_previous_position(
    position, direction, expected_new_position
):
    assert direction.get_previous_position(position) == expected_new_position


@pytest.mark.parametrize(
    "position, in_the_map",
    [
        ((0, 0), True),
        ((9, 0), True),
        ((0, 9), True),
        ((9, 9), True),
        ((0, 10), False),
        ((10, 0), False),
        ((10, 10), False),
    ],
)
def test_position_can_be_evaluated_that_is_in_a_map(position, in_the_map):
    assert MAP.is_in(position) == in_the_map


@pytest.mark.parametrize(
    "position, direction, expected_next_obstacle",
    [
        ((4, 6), Direction.UP, (4, 0)),
        ((4, 1), Direction.RIGHT, (9, 1)),
        ((8, 1), Direction.DOWN, (8, 7)),
        ((8, 6), Direction.LEFT, (1, 6)),
    ],
)
def test_map_can_evaluate_next_obstacle_of_guard(
    position, direction, expected_next_obstacle
):
    assert (
        MAP.get_guard_next_obstacle(position, direction)
        == expected_next_obstacle
    )


def test_map_can_compute_lines_that_guard_will_travel():
    assert MAP.get_traveling_lines() == [
        Line((4, 6), (4, 1), direction=Direction.UP),  # 1st
        Line((4, 1), (8, 1), direction=Direction.RIGHT),  # 2nd
        Line((8, 1), (8, 6), direction=Direction.DOWN),  # 3rd
        Line((8, 6), (2, 6), direction=Direction.LEFT),  # 4th
        Line((2, 6), (2, 4), direction=Direction.UP),  # 5th
        Line((2, 4), (6, 4), direction=Direction.RIGHT),  # 6th
        Line((6, 4), (6, 8), direction=Direction.DOWN),  # 7th
        Line((6, 8), (1, 8), direction=Direction.LEFT),  # 8th
        Line((1, 8), (1, 7), direction=Direction.UP),  # 9th
        Line((1, 7), (7, 7), direction=Direction.RIGHT),  # 10th
        Line(  # 11 = Leaves the map line
            (7, 7), (7, 9), direction=Direction.DOWN
        ),
    ]


def test_solution_can_be_computed():
    assert compute_solution(MAP) == 41
