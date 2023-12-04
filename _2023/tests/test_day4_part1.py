import pytest
from _2023.day4 import Card, parse_input, compute_solution


def test_input_can_be_parsed(get_data):
    cards = parse_input(get_data("test_file_day4"))
    assert cards == [
        Card(
            winning_numbers=[41, 48, 83, 86, 17],
            numbers_you_have=[83, 86, 6, 31, 17, 9, 48, 53],
        ),
        Card(
            winning_numbers=[13, 32, 20, 16, 61],
            numbers_you_have=[61, 30, 68, 82, 17, 32, 24, 19],
        ),
        Card(
            winning_numbers=[1, 21, 53, 59, 44],
            numbers_you_have=[69, 82, 63, 72, 16, 21, 14, 1],
        ),
        Card(
            winning_numbers=[41, 92, 73, 84, 69],
            numbers_you_have=[59, 84, 76, 51, 58, 5, 54, 83],
        ),
        Card(
            winning_numbers=[87, 83, 26, 28, 32],
            numbers_you_have=[88, 30, 70, 12, 93, 22, 82, 36],
        ),
        Card(
            winning_numbers=[31, 18, 13, 56, 72],
            numbers_you_have=[74, 77, 10, 23, 35, 67, 36, 11],
        ),
    ]


@pytest.mark.parametrize(
    "card, expected_points",
    [
        (
            Card(
                winning_numbers=[41, 48, 83, 86, 17],
                numbers_you_have=[83, 86, 6, 31, 17, 9, 48, 53],
            ),
            8,
        ),
        (
            Card(
                winning_numbers=[13, 32, 20, 16, 61],
                numbers_you_have=[61, 30, 68, 82, 17, 32, 24, 19],
            ),
            2,
        ),
        (
            Card(
                winning_numbers=[1, 21, 53, 59, 44],
                numbers_you_have=[69, 82, 63, 72, 16, 21, 14, 1],
            ),
            2,
        ),
        (
            Card(
                winning_numbers=[41, 92, 73, 84, 69],
                numbers_you_have=[59, 84, 76, 51, 58, 5, 54, 83],
            ),
            1,
        ),
        (
            Card(
                winning_numbers=[87, 83, 26, 28, 32],
                numbers_you_have=[88, 30, 70, 12, 93, 22, 82, 36],
            ),
            0,
        ),
        (
            Card(
                winning_numbers=[31, 18, 13, 56, 72],
                numbers_you_have=[74, 77, 10, 23, 35, 67, 36, 11],
            ),
            0,
        ),
    ],
)
def test_card_can_compute_its_points(card, expected_points):
    assert card.compute_points() == expected_points


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day4")) == 13
