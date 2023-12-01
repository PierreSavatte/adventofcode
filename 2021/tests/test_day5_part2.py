import pytest
from day5.part2 import resolution, compute_points_on_line


@pytest.mark.parametrize(
    "start, end, expected_points",
    [
        ((9, 7), (7, 9), [(9, 7), (8, 8), (7, 9)]),
        ((1, 1), (3, 3), [(1, 1), (2, 2), (3, 3)]),
    ],
)
def test_45_degrees_line_is_supported_on_points_computation(
    start, end, expected_points
):
    points = list(compute_points_on_line(start, end))

    assert points == expected_points


def test_puzzle_is_resolved():
    result = resolution(
        lines=[
            [(0, 9), (5, 9)],
            [(8, 0), (0, 8)],
            [(9, 4), (3, 4)],
            [(2, 2), (2, 1)],
            [(7, 0), (7, 4)],
            [(6, 4), (2, 0)],
            [(0, 9), (2, 9)],
            [(3, 4), (1, 4)],
            [(0, 0), (8, 8)],
            [(5, 5), (8, 2)],
        ]
    )

    assert result == 12
