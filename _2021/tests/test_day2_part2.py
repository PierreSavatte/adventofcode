from _2021.day2.part2 import resolution


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

    assert solution == 900
