import pytest
from _2025.day4 import Map
from _2025.day4.part1 import compute_solution

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

SMALLEST_INPUT = """..@
@@@
@@@
"""


def compute_neighbour_count(map: Map) -> list[list[int]]:
    new_map = []
    for y, row in enumerate(map.cells):
        new_row = []
        for x, cell in enumerate(row):
            count = cell.compute_nb_roll_neighbours()
            new_row.append(count)
        new_map.append(new_row)
    return new_map


@pytest.mark.parametrize(
    "position, expected_neighbours",
    [
        ((0, 0), [(1, 0), (0, 1), (1, 1)]),
        ((1, 0), [(0, 0), (2, 0), (0, 1), (1, 1), (2, 1)]),
        ((2, 0), [(1, 0), (1, 1), (2, 1)]),
        (
            (1, 1),
            [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)],
        ),
        ((0, 2), [(0, 1), (1, 1), (1, 2)]),
        ((1, 2), [(0, 1), (1, 1), (2, 1), (0, 2), (2, 2)]),
        ((2, 2), [(1, 1), (2, 1), (1, 2)]),
    ],
)
def test_neighbours_can_be_fetched(position, expected_neighbours):
    map = Map(SMALLEST_INPUT)

    x, y = position
    assert map.get_neighbour_positions(x, y) == expected_neighbours


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            SMALLEST_INPUT,
            [
                [None, None, 2],
                [3, 6, 4],
                [3, 5, 3],
            ],
        ),
        (
            INPUT,
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
def test_nb_adjacent_roll_of_papers_can_be_computed(input, expected_output):
    map = Map(input)
    assert compute_neighbour_count(map) == expected_output


def test_solution_can_be_computed():
    assert compute_solution(Map(INPUT)) == 13
