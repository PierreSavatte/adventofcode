import pytest
from _2025.day1 import parse_instructions, rotate
from _2025.day1.part1 import compute_number_of_times_the_dial_points_to_value

TEST_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_instructions_can_be_parsed():
    assert parse_instructions(TEST_INPUT) == [
        -68,
        -30,
        48,
        -5,
        60,
        -55,
        -1,
        -99,
        14,
        -82,
    ]


@pytest.mark.parametrize(
    "start, amount, expected_result",
    [
        (11, 8, 19),
        (19, -19, 0),
        (0, -1, 99),
        (99, 1, 0),
        (5, -10, 95),
        (95, 5, 0),
    ],
)
def test_rotation_can_be_computed(start, amount, expected_result):
    assert rotate(start, amount) == expected_result


def test_number_of_times_the_dial_points_to_value_can_be_computed():
    assert (
        compute_number_of_times_the_dial_points_to_value(
            dial=50, instructions=TEST_INPUT, value=0
        )
        == 3
    )
