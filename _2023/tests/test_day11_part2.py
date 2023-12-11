import pytest

from _2023.day11.part2 import compute_solution


@pytest.mark.parametrize(
    "age, expected_solution",
    [
        (10, 1030),
        (100, 8410),
    ],
)
def test_solution_can_be_computed(get_data, age, expected_solution):
    data = get_data("test_file_day11")

    assert compute_solution(data, age=age) == expected_solution
