import pytest

from _2023.day13 import Reflection, Pattern, transpose, parse_patterns
from _2023.day13.part1 import compute_solution

PATTERN_1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#."""
TRANSPOSED_PATTERN_1 = """#.##..#
..##...
##..###
#....#.
.#..#.#
.#..#.#
#....#.
##..###
..##..."""

PATTERN_2 = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
TRANSPOSED_PATTERN_2 = """##.##.#
...##..
..####.
..####.
#..##..
##....#
..####.
..####.
###..##"""


@pytest.mark.parametrize(
    "data, expected_transposed_pattern",
    [
        (PATTERN_1, TRANSPOSED_PATTERN_1),
        (PATTERN_2, TRANSPOSED_PATTERN_2),
    ],
)
def test_pattern_can_be_transposed(data, expected_transposed_pattern):
    lines = [line for line in data.splitlines()]
    transposed_lines = transpose(lines=lines)
    transposed_patterns = "\n".join(transposed_lines)
    assert transposed_patterns == expected_transposed_pattern


@pytest.mark.parametrize(
    "pattern, expected_reflection_line",
    [
        (PATTERN_1, Reflection(x=4, y=None)),
        (PATTERN_2, Reflection(y=3, x=None)),
    ],
)
def test_reflection_line_can_be_found(pattern, expected_reflection_line):
    assert Pattern.from_data(pattern).reflection == expected_reflection_line


@pytest.mark.parametrize(
    "reflection, expected_summary",
    [
        (Reflection(x=4, y=None), 5),
        (Reflection(y=3, x=None), 400),
    ],
)
def test_reflection_can_be_summarized(reflection, expected_summary):
    assert reflection.summarize() == expected_summary


def test_input_can_be_parsed(get_data):
    assert parse_patterns(get_data("test_file_day13")) == [
        PATTERN_1,
        PATTERN_2,
    ]


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day13")) == 405
