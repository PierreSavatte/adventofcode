import pytest
from _2025.day5 import Ingredients
from _2025.day5.part2 import compute_simplified_ranges, compute_solution

INPUT = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


@pytest.mark.parametrize(
    "starting_ranges, expected_ending_ranges",
    [
        (
            # Base example
            [range(3, 6), range(10, 15), range(16, 21), range(12, 19)],
            [range(3, 6), range(10, 21)],
        ),
        (
            # If all ranges can be merged
            [range(3, 6), range(5, 15), range(16, 21), range(12, 19)],
            [range(3, 21)],
        ),
        (
            # Works with rearranged order
            [range(16, 21), range(3, 6), range(12, 19), range(5, 15)],
            [range(3, 21)],
        ),
        (
            # Are not changed if ranges can't be merged
            [range(1, 10), range(12, 15)],
            [range(1, 10), range(12, 15)],
        ),
        (
            # Are not merged if they don't intersect
            # Knowing that range(a, b) == x in [a; b[
            [range(1, 10), range(10, 15)],
            [range(1, 10), range(10, 15)],
        ),
        (
            # Are merged if they intersect with one item
            [range(1, 10), range(9, 15)],
            [range(1, 15)],
        ),
        (
            # Are merged if they intersect with one item
            [range(14, 20), range(9, 15)],
            [range(9, 20)],
        ),
        (
            # Second range is included in first one
            [range(1, 20), range(5, 19)],
            [range(1, 20)],
        ),
    ],
)
def test_ranges_can_be_simplified(starting_ranges, expected_ending_ranges):
    assert compute_simplified_ranges(starting_ranges) == expected_ending_ranges


def test_result_can_be_computed():
    ingredients = Ingredients(INPUT)
    assert compute_solution(ingredients) == 14
