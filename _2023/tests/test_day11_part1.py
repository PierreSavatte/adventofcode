import pytest

from _2023.day11 import Universe, transpose_table, manhattan_distance
from _2023.day11.part1 import compute_solution


@pytest.fixture
def expanded_universe():
    data = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""

    return Universe.from_input(data)


def test_universe_can_be_computed(get_data):
    data = get_data("test_file_day11")

    universe = Universe.from_input(data)

    assert universe.tiles


@pytest.mark.parametrize(
    "input_table, expected_transposed_table",
    [
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [
                [1, 4, 7],
                [2, 5, 8],
                [3, 6, 9],
            ],
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            [
                [1, 4],
                [2, 5],
                [3, 6],
            ],
        ),
    ],
)
def test_table_can_be_transposed(input_table, expected_transposed_table):
    assert transpose_table(input_table) == expected_transposed_table


def test_universe_can_expand(get_data, expanded_universe):
    data = get_data("test_file_day11")
    universe = Universe.from_input(data)

    assert universe.expand().tiles == expanded_universe.tiles


def test_universe_can_give_its_galaxies_positions(expanded_universe):
    assert expanded_universe.galaxy_positions == [
        (4, 0),
        (9, 1),
        (0, 2),
        (8, 5),
        (1, 6),
        (12, 7),
        (9, 10),
        (0, 11),
        (5, 11),
    ]


def test_universe_can_compute_its_pairs(expanded_universe):
    assert expanded_universe.galaxy_pairs == [
        ((4, 0), (9, 1)),
        ((4, 0), (0, 2)),
        ((4, 0), (8, 5)),
        ((4, 0), (1, 6)),
        ((4, 0), (12, 7)),
        ((4, 0), (9, 10)),
        ((4, 0), (0, 11)),
        ((4, 0), (5, 11)),
        ((9, 1), (0, 2)),
        ((9, 1), (8, 5)),
        ((9, 1), (1, 6)),
        ((9, 1), (12, 7)),
        ((9, 1), (9, 10)),
        ((9, 1), (0, 11)),
        ((9, 1), (5, 11)),
        ((0, 2), (8, 5)),
        ((0, 2), (1, 6)),
        ((0, 2), (12, 7)),
        ((0, 2), (9, 10)),
        ((0, 2), (0, 11)),
        ((0, 2), (5, 11)),
        ((8, 5), (1, 6)),
        ((8, 5), (12, 7)),
        ((8, 5), (9, 10)),
        ((8, 5), (0, 11)),
        ((8, 5), (5, 11)),
        ((1, 6), (12, 7)),
        ((1, 6), (9, 10)),
        ((1, 6), (0, 11)),
        ((1, 6), (5, 11)),
        ((12, 7), (9, 10)),
        ((12, 7), (0, 11)),
        ((12, 7), (5, 11)),
        ((9, 10), (0, 11)),
        ((9, 10), (5, 11)),
        ((0, 11), (5, 11)),
    ]


def test_manhattan_distance_can_be_computed():
    assert manhattan_distance(a=(4, 0), b=(9, 10)) == 15
    assert manhattan_distance(a=(0, 2), b=(12, 7)) == 17
    assert manhattan_distance(a=(0, 11), b=(5, 11)) == 5


def test_solution_can_be_computed(get_data):
    data = get_data("test_file_day11")

    assert compute_solution(data) == 374
