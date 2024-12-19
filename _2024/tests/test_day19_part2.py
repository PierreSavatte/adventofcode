import pytest
from _2024.day19 import ImpossiblePattern, construct_all_arrangements
from _2024.day19.part2 import compute_solution

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


@pytest.mark.parametrize(
    "pattern, expected_arrangements",
    [
        # [["br", "wr", "r"], ["b", "r", "wr", "r"]],
        ("brwrr", 2),
        #
        ("bggr", 1),
        # [
        #     ["gb", "br"],
        #     ["gb", "b", "r"],
        #     ["g", "b", "br"],
        #     ["g", "b", "b", "r"],
        # ],
        ("gbbr", 4),
        # [
        #     ["r", "rb", "gb", "r"],
        #     ["r", "rb", "g", "br"],
        #     ["r", "rb", "g", "b", "r"],
        #     ["r", "r", "b", "gb", "r"],
        #     ["r", "r", "b", "g", "br"],
        #     ["r", "r", "b", "g", "b", "r"],
        # ],
        ("rrbgbr", 6),
        # [["bwu", "r", "r", "g"]]
        ("bwurrg", 1),
        # [
        #     ["br", "g", "r"],
        #     ["b", "r", "g", "r"],
        # ],
        ("brgr", 2),
    ],
)
def test_all_arrangements_can_be_constructed(pattern, expected_arrangements):
    assert (
        construct_all_arrangements(pattern, tuple(AVAILABLE_TOWELS))
        == expected_arrangements
    )


@pytest.mark.parametrize("pattern", ["ubwu", "bbrgwb"])
def test_impossible_pattern_cannot_be_constructed(pattern):
    with pytest.raises(ImpossiblePattern):
        construct_all_arrangements(pattern, tuple(AVAILABLE_TOWELS))


def test_solution_can_be_computed():
    assert compute_solution(AVAILABLE_TOWELS, PATTERNS) == 16
