import pytest

from _2023.day12.part2 import compute_solution, compute_unfolded_arrangements


@pytest.mark.parametrize(
    "line, expected_number_of_arrangements",
    [
        ("???.### 1,1,3", 1),
        (".??..??...?##. 1,1,3", 16384),
        ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        ("????.#...#... 4,1,1", 16),
        ("????.######..#####. 1,6,5", 2500),
        ("?###???????? 3,2,1", 506250),
    ],
)
def test_number_of_arrangements_can_be_computed_from_line(
    line, expected_number_of_arrangements
):
    assert (
        compute_unfolded_arrangements(line) == expected_number_of_arrangements
    )


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day12")) == 525152
