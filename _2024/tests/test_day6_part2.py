import pytest
from _2024.day6 import Direction, Line, Map


def test_direction_can_return_all_members():
    assert Direction.all() == {
        Direction.UP,
        Direction.DOWN,
        Direction.LEFT,
        Direction.RIGHT,
    }


@pytest.mark.parametrize(
    "direction, opposite",
    [
        (Direction.UP, Direction.DOWN),
        (Direction.DOWN, Direction.UP),
        (Direction.LEFT, Direction.RIGHT),
        (Direction.RIGHT, Direction.LEFT),
    ],
)
def test_direction_can_return_its_opposite(direction, opposite):
    assert direction.opposite == opposite


@pytest.mark.parametrize(
    "line_a, line_b, intersection_point",
    [
        (
            Line((0, 0), (10, 0), Direction.UP),
            Line((0, 0), (0, 10), Direction.UP),
            (0, 0),
        ),
        (
            Line((0, 0), (10, 0), Direction.UP),
            Line((5, 0), (5, 10), Direction.UP),
            (5, 0),
        ),
        (
            Line((0, 0), (10, 0), Direction.UP),
            Line((1, 1), (1, 10), Direction.UP),
            (1, 0),
        ),
    ],
)
def test_intersection_can_be_evaluated_between_two_lines(
    line_a, line_b, intersection_point
):
    assert line_a.get_intersection_point(line_b) == intersection_point
    assert line_b.get_intersection_point(line_a) == intersection_point


@pytest.mark.parametrize(
    "line_a, line_b",
    [
        (
            Line((0, 0), (10, 0), Direction.UP),
            Line((0, 1), (10, 1), Direction.UP),
        ),
        (
            Line((0, 0), (0, 10), Direction.UP),
            Line((1, 0), (1, 10), Direction.UP),
        ),
    ],
)
def test_none_is_evaluated_when_no_intersection_exists_between_two_lines(
    line_a, line_b
):
    assert line_a.get_intersection_point(line_b) is None
    assert line_b.get_intersection_point(line_a) is None


def test_loop_numbers_can_be_computed():
    map = Map(
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
    assert map.compute_loop_numbers() == 6
