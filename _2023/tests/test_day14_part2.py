import pytest

from _2023.day14 import Platform
from _2023.day14.part2 import compute_solution


AFTER_1_CYCLE = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#...."""

AFTER_2_CYCLES = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O"""

AFTER_3_CYCLES = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O"""


def test_cycle_can_be_executed(get_data):
    data = get_data("test_file_day14")
    platform = Platform.from_input(data=data)

    platform = platform.spin_cycle()

    assert platform.as_str() == AFTER_1_CYCLE


@pytest.mark.parametrize(
    "n, expected_result",
    [
        (2, AFTER_2_CYCLES),
        (3, AFTER_3_CYCLES),
    ],
)
def test_cycle_can_be_executed_multiple_times(get_data, n, expected_result):
    data = get_data("test_file_day14")
    platform = Platform.from_input(data=data)

    platform = platform.spin_cycle(n=n)

    assert platform.as_str() == expected_result


def test_solution_can_be_computed(get_data):
    data = get_data("test_file_day14")
    assert compute_solution(data) == 64
