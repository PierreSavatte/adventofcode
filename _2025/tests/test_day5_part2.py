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


def test_ranges_can_be_simplified():
    assert compute_simplified_ranges(
        [range(3, 6), range(10, 15), range(16, 21), range(12, 19)]
    ) == [range(3, 6), range(10, 21)]


def test_result_can_be_computed():
    ingredients = Ingredients(INPUT)
    assert compute_solution(ingredients) == 14
