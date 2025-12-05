import pytest
from _2025.day4 import (
    compute_neighbour_count,
    compute_solution,
    get_neighbours,
    mark,
    parse_map,
)

INPUT = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

MAP = [
    [".", ".", "@", "@", ".", "@", "@", "@", "@", "."],
    ["@", "@", "@", ".", "@", ".", "@", ".", "@", "@"],
    ["@", "@", "@", "@", "@", ".", "@", ".", "@", "@"],
    ["@", ".", "@", "@", "@", "@", ".", ".", "@", "."],
    ["@", "@", ".", "@", "@", "@", "@", ".", "@", "@"],
    [".", "@", "@", "@", "@", "@", "@", "@", ".", "@"],
    [".", "@", ".", "@", ".", "@", ".", "@", "@", "@"],
    ["@", ".", "@", "@", "@", ".", "@", "@", "@", "@"],
    [".", "@", "@", "@", "@", "@", "@", "@", "@", "."],
    ["@", ".", "@", ".", "@", "@", "@", ".", "@", "."],
]


def test_map_can_be_parsed():
    assert parse_map(INPUT) == MAP


@pytest.mark.parametrize(
    "position, expected_neighbours",
    [
        ((0, 0), [".", "@", "@"]),
        ((1, 0), [".", "@", "@", "@", "@"]),
        ((2, 0), [".", "@", "@"]),
        ((0, 1), [".", ".", "@", "@", "@"]),
        ((1, 1), [".", ".", "@", "@", "@", "@", "@", "@"]),
        ((2, 1), [".", "@", "@", "@", "@"]),
        ((0, 2), ["@", "@", "@"]),
        ((1, 2), ["@", "@", "@", "@", "@"]),
        ((2, 2), ["@", "@", "@"]),
    ],
)
def test_neighbours_can_be_fetched(position, expected_neighbours):
    map = [
        [".", ".", "@"],
        ["@", "@", "@"],
        ["@", "@", "@"],
    ]

    x, y = position
    assert get_neighbours(map, x, y) == expected_neighbours


@pytest.mark.parametrize(
    "map, expected_output",
    [
        (
            [
                [".", ".", "@"],
                ["@", "@", "@"],
                ["@", "@", "@"],
            ],
            [
                [None, None, 2],
                [3, 6, 4],
                [3, 5, 3],
            ],
        ),
        (
            MAP,
            [
                [None, None, 3, 3, None, 3, 3, 4, 3, None],
                [3, 6, 6, None, 4, None, 4, None, 5, 4],
                [4, 7, 6, 7, 5, None, 2, None, 4, 4],
                [4, None, 6, 7, 7, 6, None, None, 4, None],
                [3, 5, None, 7, 8, 7, 5, None, 4, 3],
                [None, 4, 6, 5, 7, 6, 6, 5, None, 4],
                [None, 4, None, 6, None, 5, None, 6, 7, 4],
                [2, None, 6, 6, 6, None, 6, 7, 7, 4],
                [None, 5, 5, 7, 6, 7, 6, 7, 5, None],
                [1, None, 3, None, 4, 5, 4, None, 2, None],
            ],
        ),
    ],
)
def test_nb_adjacent_roll_of_papers_can_be_computed(map, expected_output):
    assert compute_neighbour_count(map) == expected_output


def test_map_can_be_marked_with_position_that_has_not_too_much_neighbours():
    expected_marked_map = [
        "..xx.xx@x.\n",
        "x@@.@.@.@@\n",
        "@@@@@.x.@@\n",
        "@.@@@@..@.\n",
        "x@.@@@@.@x\n",
        ".@@@@@@@.@\n",
        ".@.@.@.@@@\n",
        "x.@@@.@@@@\n",
        ".@@@@@@@@.\n",
        "x.x.@@@.x.\n",
    ]

    assert mark(MAP) == expected_marked_map


def test_solution_can_be_computed():
    assert compute_solution(MAP) == 13
