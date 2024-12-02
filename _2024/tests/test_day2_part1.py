import pytest
from _2024.day2 import (
    are_adjacent_levels_safe,
    are_levels_strictly_monotonic,
    is_safe,
    parse_input,
)
from _2024.day2.part1 import count_safe_reports

TEST_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


@pytest.mark.parametrize(
    "levels, expected_is_safe",
    [
        ((7, 6), True),
        ((6, 4), True),
        ((4, 2), True),
        ((2, 1), True),
        ((2, 7), False),
        ((6, 2), False),
    ],
)
def test_safeness_of_adjacent_levels_can_be_evaluated(
    levels, expected_is_safe
):
    assert are_adjacent_levels_safe(*levels) == expected_is_safe


@pytest.mark.parametrize(
    "levels, expected_monotonic",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], True),
        ([9, 7, 6, 2, 1], True),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_evaluation_of_monotonic_of_a_function_can_be_evaluated(
    levels, expected_monotonic
):
    assert are_levels_strictly_monotonic(levels) == expected_monotonic


@pytest.mark.parametrize(
    "levels, expected_is_safe",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_safeness_of_reports_can_be_evaluated(levels, expected_is_safe):
    assert is_safe(levels) == expected_is_safe


def test_sum_of_safeness_of_reports_can_be_computed():
    assert count_safe_reports(TEST_INPUT) == 2
