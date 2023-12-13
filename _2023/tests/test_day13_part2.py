import pytest

from _2023.day13 import Reflection, Pattern
from _2023.day13.part2 import compute_solution

PATTERN_1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#."""

PATTERN_2 = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


@pytest.mark.parametrize(
    "pattern, expected_reflection_line",
    [
        (PATTERN_1, Reflection(y=2, x=None)),
        (PATTERN_2, Reflection(y=0, x=None)),
    ],
)
def test_reflection_line_can_be_found(pattern, expected_reflection_line):
    assert (
        Pattern.from_data(pattern, fix_smudge=True).reflection
        == expected_reflection_line
    )


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day13")) == 400
