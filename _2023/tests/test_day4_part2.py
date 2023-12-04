import pytest

from _2023.day4 import Card, parse_input
from _2023.day4.part2 import Deck, compute_solution

CARD_1 = Card(
    number=1,
    winning_numbers=[41, 48, 83, 86, 17],
    numbers_you_have=[83, 86, 6, 31, 17, 9, 48, 53],
)
CARD_2 = Card(
    number=2,
    winning_numbers=[13, 32, 20, 16, 61],
    numbers_you_have=[61, 30, 68, 82, 17, 32, 24, 19],
)
CARD_3 = Card(
    number=3,
    winning_numbers=[1, 21, 53, 59, 44],
    numbers_you_have=[69, 82, 63, 72, 16, 21, 14, 1],
)
CARD_4 = Card(
    number=4,
    winning_numbers=[41, 92, 73, 84, 69],
    numbers_you_have=[59, 84, 76, 51, 58, 5, 54, 83],
)
CARD_5 = Card(
    number=5,
    winning_numbers=[87, 83, 26, 28, 32],
    numbers_you_have=[88, 30, 70, 12, 93, 22, 82, 36],
)
CARD_6 = Card(
    number=6,
    winning_numbers=[31, 18, 13, 56, 72],
    numbers_you_have=[74, 77, 10, 23, 35, 67, 36, 11],
)


@pytest.mark.parametrize(
    "card, expected_copies_won",
    [
        (CARD_1, 4),
        (CARD_2, 2),
        (CARD_3, 2),
        (CARD_4, 1),
        (CARD_5, 0),
        (CARD_6, 0),
    ],
)
def test_card_can_compute_its_numbers_of_matches(card, expected_copies_won):
    assert card.compute_match_numbers() == expected_copies_won


def test_deck_can_be_computed(get_data):
    cards = parse_input(get_data("test_file_day4"))
    assert Deck.from_cards(cards).mapping == {
        1: 1,
        2: 2,
        3: 4,
        4: 8,
        5: 14,
        6: 1,
    }


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day4")) == 30
