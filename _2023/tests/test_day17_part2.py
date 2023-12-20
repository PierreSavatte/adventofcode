import pytest

from _2023.day17.part2 import compute_solution


@pytest.mark.parametrize(
    "data_filename, expected_result",
    [
        ("test_file_day17_part1", 94),
        ("test_file_day17_part2", 63),
    ],
)
def test_solution_can_be_computed(get_data, data_filename, expected_result):
    assert compute_solution(get_data(data_filename)) == expected_result
