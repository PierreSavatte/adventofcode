from _2024.day3 import parse_input
from _2024.day3.part1 import REGEX, compute_solution

TEST_INPUT = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT, regex=REGEX) == [
        (2, 4),
        (5, 5),
        (11, 8),
        (8, 5),
    ]


def test_solution_can_be_computed():
    groups = [
        (2, 4),
        (5, 5),
        (11, 8),
        (8, 5),
    ]
    assert compute_solution(groups) == 161
