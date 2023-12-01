from _2021.day7.part2 import resolution


def test_puzzle_is_resolved():
    result = resolution([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

    assert result == 168
