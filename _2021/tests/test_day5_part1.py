import os

import pytest

from _2021.day5.part1 import parse_file, compute_points_on_line, resolution


def test_file_is_parsed_correctly():
    data = parse_file(os.path.join("data", "test_file_day5"))

    assert data == [
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


@pytest.mark.parametrize(
    "start, end, expected_points",
    [
        ((1, 1), (1, 3), [(1, 1), (1, 2), (1, 3)]),
        ((9, 7), (7, 7), [(9, 7), (8, 7), (7, 7)]),
    ],
)
def test_points_on_line_are_computed_from_start_and_end_points(
    start, end, expected_points
):
    points = compute_points_on_line(start, end)

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

    assert result == 5
