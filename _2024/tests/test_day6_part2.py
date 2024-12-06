import pytest
from _2024.day6 import Line


@pytest.mark.parametrize(
    "line_a, line_b, intersection_point",
    [
        (Line((0, 0), (10, 0)), Line((0, 0), (0, 10)), (0, 0)),
        (Line((0, 0), (10, 0)), Line((5, 0), (5, 10)), (5, 0)),
        (Line((0, 0), (10, 0)), Line((1, 1), (1, 10)), (1, 0)),
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
        (Line((0, 0), (10, 0)), Line((0, 1), (10, 1))),
        (Line((0, 0), (0, 10)), Line((1, 0), (1, 10))),
    ],
)
def test_none_is_evaluated_when_no_intersection_exists_between_two_lines(
    line_a, line_b
):
    assert line_a.get_intersection_point(line_b) is None
    assert line_b.get_intersection_point(line_a) is None
