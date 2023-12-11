import pytest

from _2023.day11 import expand_lines_of_table
from _2023.day11.part2 import compute_solution


def test_lines_of_table_can_be_expanded_based_on_age():
    table = [
        [".", ".", "."],
        [".", "#", "."],
        [".", ".", "."],
        [".", "#", "."],
    ]
    expected_result = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", "#", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", "#", "."],
    ]
    assert expand_lines_of_table(table, age=10) == expected_result


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
