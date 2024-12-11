import pytest
from _2024.day11 import change, change_stone, parse_input
from _2024.day11.part1 import compute_solution

TEST_INPUT = """0 1 10 99 999
"""


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == [0, 1, 10, 99, 999]


@pytest.mark.parametrize(
    "stone, new_stones",
    [
        (0, [1]),
        (1, [2024]),
        (10, [1, 0]),
        (99, [9, 9]),
        (999, [2021976]),
        (1000, [10, 0]),
    ],
)
def test_stone_can_change_according_to_the_rules(stone, new_stones):
    assert change_stone(stone) == new_stones


@pytest.mark.parametrize(
    "stones, next_stones",
    [
        ([125, 17], [253000, 1, 7]),
        ([253000, 1, 7], [253, 0, 2024, 14168]),
        ([253, 0, 2024, 14168], [512072, 1, 20, 24, 28676032]),
        (
            [512072, 1, 20, 24, 28676032],
            [512, 72, 2024, 2, 0, 2, 4, 2867, 6032],
        ),
        (
            [512, 72, 2024, 2, 0, 2, 4, 2867, 6032],
            [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32],
        ),
        (
            [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32],
            [
                2097446912,
                14168,
                4048,
                2,
                0,
                2,
                4,
                40,
                48,
                2024,
                40,
                48,
                80,
                96,
                2,
                8,
                6,
                7,
                6,
                0,
                3,
                2,
            ],
        ),
    ],
)
def test_stones_can_change_according_to_the_rules(stones, next_stones):
    assert change(stones) == next_stones


def test_solution_can_be_computed():
    assert compute_solution([125, 17], nb_change=25) == 55312
