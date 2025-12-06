import pytest
from _2025.day5 import Ingredients
from _2025.day5.part1 import compute_solution

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


def test_input_can_be_parsed():
    ingredients = Ingredients(INPUT)

    assert ingredients.ranges == [
        range(3, 6),
        range(10, 15),
        range(16, 21),
        range(12, 19),
    ]
    assert ingredients.availables == [1, 5, 8, 11, 17, 32]


@pytest.mark.parametrize(
    "ingredient, expected_is_fresh",
    [
        (1, False),
        (5, True),
        (8, False),
        (11, True),
        (17, True),
        (32, False),
    ],
)
def test_ingredient_can_be_tested_as_fresh(ingredient, expected_is_fresh):
    ingredients = Ingredients(INPUT)
    assert ingredients.is_fresh(ingredient) == expected_is_fresh


def test_result_can_be_computed():
    ingredients = Ingredients(INPUT)
    assert compute_solution(ingredients) == 3
