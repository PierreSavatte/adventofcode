import pytest
from _2024.day6 import Direction, Line, Map, Ray

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
    "line, ray",
    [
        (
            Line((4, 6), (4, 1), direction=Direction.UP),
            Ray(start=(4, 1), direction=Direction.DOWN),
        ),
        (
            Line((4, 1), (8, 1), direction=Direction.RIGHT),
            Ray(start=(8, 1), direction=Direction.LEFT),
        ),
    ],
)
def test_line_can_compute_its_ray(line, ray):
    assert line.get_ray() == ray


@pytest.mark.parametrize(
    "ray, end",
    [
        (Ray(start=(1, 1), direction=Direction.UP), (1, 0)),
        (Ray(start=(1, 1), direction=Direction.DOWN), (1, 9)),
        (Ray(start=(1, 1), direction=Direction.LEFT), (0, 1)),
        (Ray(start=(1, 1), direction=Direction.RIGHT), (9, 1)),
    ],
)
def test_ray_can_compute_its_end(ray, end):
    assert ray.compute_end(map_size=10) == end


@pytest.mark.parametrize(
    "line, ray, intersection_point",
    [
        (
            Line((8, 6), (2, 6), direction=Direction.LEFT),  # 4th
            Ray((4, 1), direction=Direction.DOWN),  # 1st
            (4, 6),
        ),
        (
            Line((6, 4), (6, 8), direction=Direction.DOWN),  # 7th
            Ray((2, 6), direction=Direction.RIGHT),  # 4th
            (6, 6),
        ),
        (
            Line((1, 7), (7, 7), direction=Direction.RIGHT),  # 10th
            Ray((6, 8), direction=Direction.UP),  # 7th
            (6, 7),
        ),
        (
            Line((6, 8), (1, 8), direction=Direction.LEFT),  # 8th
            Ray((2, 4), direction=Direction.DOWN),  # 5th
            (2, 8),
        ),
        (
            Line((6, 8), (1, 8), direction=Direction.LEFT),  # 8th
            Ray((4, 1), direction=Direction.DOWN),  # 1st
            (4, 8),
        ),
        (
            Line((7, 7), (7, 9), direction=Direction.DOWN),  # 11th
            Ray((1, 8), direction=Direction.RIGHT),  # 8th
            (7, 8),
        ),
    ],
)
def test_intersection_can_be_evaluated_between_a_line_and_a_ray(
    line, ray, intersection_point
):
    assert line.get_intersection_point(ray, map_size=10) == intersection_point


@pytest.mark.parametrize(
    "line, ray",
    [
        (
            Line(start=(8, 1), end=(8, 6), direction=Direction.DOWN),
            Ray(start=(4, 1), direction=Direction.DOWN),
        ),
        (
            Line(start=(8, 6), end=(2, 6), direction=Direction.LEFT),
            Ray(start=(8, 1), direction=Direction.LEFT),
        ),
        (
            Line(start=(2, 6), end=(2, 4), direction=Direction.UP),
            Ray(start=(4, 1), direction=Direction.DOWN),
        ),
        (
            Line(start=(2, 6), end=(2, 4), direction=Direction.UP),
            Ray(start=(8, 1), direction=Direction.LEFT),
        ),
        (
            Line(start=(2, 6), end=(2, 4), direction=Direction.UP),
            Ray(start=(8, 6), direction=Direction.UP),
        ),
        (
            Line(start=(2, 4), end=(6, 4), direction=Direction.RIGHT),
            Ray(start=(4, 1), direction=Direction.DOWN),
        ),
        (
            Line(start=(2, 4), end=(6, 4), direction=Direction.RIGHT),
            Ray(start=(8, 1), direction=Direction.LEFT),
        ),
        (
            Line(start=(2, 4), end=(6, 4), direction=Direction.RIGHT),
            Ray(start=(8, 6), direction=Direction.UP),
        ),
        (
            Line(start=(2, 4), end=(6, 4), direction=Direction.RIGHT),
            Ray(start=(2, 6), direction=Direction.RIGHT),
        ),
        (
            Line(start=(6, 4), end=(6, 8), direction=Direction.DOWN),
            Ray(start=(4, 1), direction=Direction.DOWN),
        ),
        (
            Line(start=(6, 4), end=(6, 8), direction=Direction.DOWN),
            Ray(start=(8, 1), direction=Direction.LEFT),
        ),
        (
            Line(start=(6, 4), end=(6, 8), direction=Direction.DOWN),
            Ray(start=(8, 6), direction=Direction.UP),
        ),
        (
            Line(start=(6, 4), end=(6, 8), direction=Direction.DOWN),
            Ray(start=(2, 4), direction=Direction.DOWN),
        ),
        (
            Line(start=(6, 8), end=(1, 8), direction=Direction.LEFT),
            Ray(start=(8, 1), direction=Direction.LEFT),
        ),
        (
            Line(start=(6, 8), end=(1, 8), direction=Direction.LEFT),
            Ray(start=(8, 6), direction=Direction.UP),
        ),
        (
            Line(start=(6, 8), end=(1, 8), direction=Direction.LEFT),
            Ray(start=(2, 6), direction=Direction.RIGHT),
        ),
        (
            Line(start=(6, 8), end=(1, 8), direction=Direction.LEFT),
            Ray(start=(6, 4), direction=Direction.LEFT),
        ),
        (
            Line(start=(1, 8), end=(1, 7), direction=Direction.UP),
            Ray(start=(4, 1), direction=Direction.DOWN),
        ),
        (
            Line(start=(1, 8), end=(1, 7), direction=Direction.UP),
            Ray(start=(8, 1), direction=Direction.LEFT),
        ),
        (
            Line(start=(1, 8), end=(1, 7), direction=Direction.UP),
            Ray(start=(8, 6), direction=Direction.UP),
        ),
        (
            Line(start=(1, 8), end=(1, 7), direction=Direction.UP),
            Ray(start=(2, 6), direction=Direction.RIGHT),
        ),
        (
            Line(start=(1, 8), end=(1, 7), direction=Direction.UP),
            Ray(start=(2, 4), direction=Direction.DOWN),
        ),
        (
            Line(start=(1, 8), end=(1, 7), direction=Direction.UP),
            Ray(start=(6, 4), direction=Direction.LEFT),
        ),
        (
            Line(start=(1, 8), end=(1, 7), direction=Direction.UP),
            Ray(start=(6, 8), direction=Direction.UP),
        ),
        (
            Line(start=(1, 7), end=(7, 7), direction=Direction.RIGHT),
            Ray(start=(4, 1), direction=Direction.DOWN),
        ),
        (
            Line(start=(1, 7), end=(7, 7), direction=Direction.RIGHT),
            Ray(start=(8, 1), direction=Direction.LEFT),
        ),
        (
            Line(start=(1, 7), end=(7, 7), direction=Direction.RIGHT),
            Ray(start=(8, 6), direction=Direction.UP),
        ),
        (
            Line(start=(1, 7), end=(7, 7), direction=Direction.RIGHT),
            Ray(start=(2, 6), direction=Direction.RIGHT),
        ),
        (
            Line(start=(1, 7), end=(7, 7), direction=Direction.RIGHT),
            Ray(start=(2, 4), direction=Direction.DOWN),
        ),
        (
            Line(start=(1, 7), end=(7, 7), direction=Direction.RIGHT),
            Ray(start=(6, 4), direction=Direction.LEFT),
        ),
        (
            Line(start=(1, 7), end=(7, 7), direction=Direction.RIGHT),
            Ray(start=(1, 8), direction=Direction.RIGHT),
        ),
    ],
)
def test_intersection_cannot_be_found_on_cases_where_there_there_shouldnt_be_any(  # noqa: E501
    line, ray
):
    assert line.get_intersection_point(ray, map_size=10) is None


def test_loop_numbers_can_be_computed():
    assert MAP.compute_loop_numbers() == 6
