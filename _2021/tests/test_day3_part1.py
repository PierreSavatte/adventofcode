import os

from _2021.day3.part1 import resolution


def test_puzzle_is_resolved():
    result = resolution(os.path.join("data", "test_file_day3"))

    assert result == 198
