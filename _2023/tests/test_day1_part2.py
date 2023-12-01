import pytest

from _2023.day1.part2 import parse_line, compute_answer


@pytest.mark.parametrize(
    "line, expected_value",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_line_is_properly_parsed(line, expected_value):
    assert parse_line(line) == expected_value


def test_answer_can_be_computed(get_data):
    assert compute_answer(get_data("test_file_day1_part2")) == 281
