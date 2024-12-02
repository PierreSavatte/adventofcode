import pytest
from _2024.day2.part2 import (
    MonotonicType,
    count_safe_reports_with_problem_dampener,
    evaluate_monotonic_type,
    is_safe_with_problem_dampener,
)

TEST_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


@pytest.mark.parametrize(
    "levels, expected_monotonic_type",
    [
        ([7, 6, 4, 2, 1], MonotonicType.STRICTLY_DECREASING),
        ([1, 2, 7, 8, 9], MonotonicType.STRICTLY_INCREASING),
        ([9, 7, 6, 2, 1], MonotonicType.STRICTLY_DECREASING),
        ([1, 3, 2, 4, 5], MonotonicType.STRICTLY_INCREASING),
        ([8, 6, 4, 4, 1], MonotonicType.STRICTLY_DECREASING),
        ([1, 3, 6, 7, 9], MonotonicType.STRICTLY_INCREASING),
    ],
)
def test_monotonic_type_can_be_evaluated_on_report(
    levels, expected_monotonic_type
):
    assert evaluate_monotonic_type(levels) == expected_monotonic_type


@pytest.mark.parametrize(
    "levels, expected_is_safe",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_safeness_of_reports_can_be_evaluated_with_problem_dampener(
    levels, expected_is_safe
):
    assert is_safe_with_problem_dampener(levels) == expected_is_safe


def test_sum_of_safeness_of_reports_can_be_computed():
    assert count_safe_reports_with_problem_dampener(TEST_INPUT) == 4
