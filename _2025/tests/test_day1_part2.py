import pytest
from _2025.day1 import parse_instructions
from _2025.day1.part2 import Safe

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
    "start, instruction, expected_result",
    [
        (50, -68, 1),
        (95, 60, 1),
        (0, -5, 0),
        (14, -82, 1),
        (50, 1000, 10),
        (82, -30, 0),
    ],
)
def test_number_of_times_dial_goes_to_0_can_be_counted(
    start, instruction, expected_result
):
    safe = Safe(start)

    safe.execute(instruction)

    assert safe.number_of_times_dial_goes_to_0 == expected_result


def test_total_number_of_times_dial_goes_to_0_can_be_counted():
    safe = Safe()

    safe.execute_all(parse_instructions(TEST_INPUT))

    assert safe.get_password() == 6
