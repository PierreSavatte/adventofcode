import pytest
from _2024.day19 import ImpossiblePattern, construct_pattern, parse_input
from _2024.day19.part1 import compute_solution

TEST_INPUT = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""
AVAILABLE_TOWELS = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
PATTERNS = [
    "brwrr",
    "bggr",
    "gbbr",
    "rrbgbr",
    "ubwu",
    "bwurrg",
    "brgr",
    "bbrgwb",
]


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == (AVAILABLE_TOWELS, PATTERNS)


@pytest.mark.parametrize(
    "pattern, expected_towels_used",
    [
        ("brwrr", ["br", "wr", "r"]),
        ("bggr", ["b", "g", "g", "r"]),
        ("gbbr", ["gb", "br"]),
        ("bwurrg", ["bwu", "r", "r", "g"]),
        ("brgr", ["br", "g", "r"]),
    ],
)
def test_pattern_can_be_constructed(pattern, expected_towels_used):
    assert construct_pattern(pattern, AVAILABLE_TOWELS) == expected_towels_used


@pytest.mark.parametrize("pattern", ["ubwu", "bbrgwb"])
def test_impossible_pattern_cannot_be_constructed(pattern):
    with pytest.raises(ImpossiblePattern):
        construct_pattern(pattern, AVAILABLE_TOWELS)


def test_solution_can_be_computed():
    assert compute_solution(AVAILABLE_TOWELS, PATTERNS) == 6
