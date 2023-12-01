import pytest

from _2023.day1 import parse_line, compute_answer


@pytest.mark.parametrize(
    "line, expected_value",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_line_is_properly_parsed(line, expected_value):
    assert parse_line(line) == expected_value


def test_answer_can_be_computed(get_data):
    assert compute_answer(get_data("test_file_day1")) == 142
