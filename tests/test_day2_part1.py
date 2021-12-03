import os

from day2.part1 import resolution, parse_file


def test_puzzle_is_resolved():
    instructions = [
        ("x", 5),
        ("z", 5),
        ("x", 8),
        ("z", -3),
        ("z", 8),
        ("x", 2),
    ]

    solution = resolution(instructions)

    assert solution == 150


def test_file_is_correctly_parsed():
    result = parse_file(os.path.join("data", "test_file_day2"))

    assert result == [
        ("x", 5),
        ("z", 5),
        ("x", 8),
        ("z", -3),
        ("z", 8),
        ("x", 2),
    ]
