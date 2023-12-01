import os

from _2021.day1.part1 import resolution, parse_file


def test_puzzle_is_resolved():
    depth_series = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    solution = resolution(depth_series)

    assert solution == 7


def test_file_is_correctly_parsed():
    result = parse_file(os.path.join("data", "test_file_day1"))

    assert result == [141, 152, 164, 163, 164, 179, 210, 209, 208, 236]
