import pytest
from _2025.day3 import get_max_joltage, get_total_joltage_output, parse_input

TEST_INPUT = """987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]


@pytest.mark.parametrize(
    "batteries, expected_result",
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_largest_joltage_can_be_found(batteries, expected_result):
    assert get_max_joltage(batteries) == expected_result


def test_total_joltage_output_can_be_computed():
    assert (
        get_total_joltage_output(
            [
                "987654321111111",
                "811111111111119",
                "234234234234278",
                "818181911112111",
            ]
        )
        == 357
    )
