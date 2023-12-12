import pytest
from _2023.day12 import (
    compute_arrangements,
    compute_total_arrangements,
    smart_split,
)


from _2023.day12.part1 import compute_solution


@pytest.mark.parametrize(
    "string, expected_splits",
    [
        (".###.##.#...", ["###", "##", "#"]),
        ("?#?#?#?#?#?#?#?", ["?#?#?#?#?#?#?#?"]),
        ("........", []),
        ("#########", ["#########"]),
    ],
)
def test_smart_split_can_be_applied_to_string(string, expected_splits):
    assert smart_split(string) == expected_splits


def test_arrangements_can_be_computed_from_input_line():
    input_line = "?###???????? 3,2,1"
    assert sorted(compute_arrangements(input_line)) == sorted(
        [
            ".###.##.#...",
            ".###.##..#..",
            ".###.##...#.",
            ".###.##....#",
            ".###..##.#..",
            ".###..##..#.",
            ".###..##...#",
            ".###...##.#.",
            ".###...##..#",
            ".###....##.#",
        ]
    )


@pytest.mark.parametrize(
    "input_line, expected_arrangements",
    [
        ("???.### 1,1,3", 1),
        (".??..??...?##. 1,1,3", 4),
        ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        ("????.#...#... 4,1,1", 1),
        ("????.######..#####. 1,6,5", 4),
        ("?###???????? 3,2,1", 10),
    ],
)
def test_total_arrangements_can_be_computed_from_input_line(
    input_line, expected_arrangements
):
    assert compute_total_arrangements(input_line) == expected_arrangements


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day12")) == 21
