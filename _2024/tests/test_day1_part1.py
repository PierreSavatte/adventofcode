import pytest
from _2024.day1 import parse_input, sort
from _2024.day1.part1 import (
    get_distance_between_lists,
    get_distance_between_values,
)

TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])


def test_list_can_be_sorted():
    assert sort([3, 4, 2, 1, 3, 3]) == [1, 2, 3, 3, 3, 4]


@pytest.mark.parametrize(
    "a, b, expected_distance",
    [
        (1, 3, 2),
        (2, 3, 1),
        (3, 2, 1),
        (3, 3, 0),
        (3, 4, 1),
        (3, 5, 2),
        (4, 9, 5),
        (9, 4, 5),
    ],
)
def test_distance_can_be_computed(a, b, expected_distance):
    assert get_distance_between_values(a, b) == expected_distance


def test_total_distance_can_be_computed():
    assert (
        get_distance_between_lists([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
        == 11
    )
