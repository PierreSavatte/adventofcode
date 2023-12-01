import os

import pytest

from day7.part1 import parse_file, median, resolution


def test_file_is_parsed_correctly():
    data = parse_file(os.path.join("data", "test_file_day7"))

    assert data == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


@pytest.mark.parametrize(
    "list,expected_result",
    [
        [[0, 0], 0],
        [[4, 3, 2, 1], 3],
        [[1, 5, 10, 20], 10],
    ],
)
def test_mean_can_be_computed(list, expected_result):
    assert median(list) == expected_result


def test_puzzle_is_resolved():
    result = resolution([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

    assert result == 37
