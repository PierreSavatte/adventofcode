import pytest

from _2023.day7 import Card, Hand, HandType, parse_input
from _2023.day7.part2 import compute_solution

A = Card(face_value="A", spicy_rules=True)
K = Card(face_value="K", spicy_rules=True)
Q = Card(face_value="Q", spicy_rules=True)
T = Card(face_value="T", spicy_rules=True)
_9 = Card(face_value="9", spicy_rules=True)
_8 = Card(face_value="8", spicy_rules=True)
_7 = Card(face_value="7", spicy_rules=True)
_6 = Card(face_value="6", spicy_rules=True)
_5 = Card(face_value="5", spicy_rules=True)
_4 = Card(face_value="4", spicy_rules=True)
_3 = Card(face_value="3", spicy_rules=True)
_2 = Card(face_value="2", spicy_rules=True)
J = Card(face_value="J", spicy_rules=True)


def test_cards_are_sortable():
    assert A > K > Q > T > _9 > _8 > _7 > _6 > _5 > _4 > _3 > _2 > J

    assert J < _2 < _3 < _4 < _5 < _6 < _7 < _8 < _9 < T < Q < K < A


ONE_PAIR = Hand(cards=[_3, _2, T, _3, K], spicy_rules=True)
TWO_PAIR = Hand(cards=[K, K, _6, _7, _7], spicy_rules=True)
FOUR_OF_A_KIND_1 = Hand(cards=[T, _5, _5, J, _5], spicy_rules=True)
FOUR_OF_A_KIND_2 = Hand(cards=[Q, Q, Q, J, A], spicy_rules=True)
FOUR_OF_A_KIND_3 = Hand(cards=[K, T, J, J, T], spicy_rules=True)


@pytest.mark.parametrize(
    "hand, expected_hand_type",
    [
        (TWO_PAIR, HandType.TWO_PAIR),
        (ONE_PAIR, HandType.ONE_PAIR),
        (
            Hand.from_input_line("JJJJJ 847", spicy_rules=True),
            HandType.FIVE_OF_A_KIND,
        ),
        (
            Hand.from_input_line("JAJJJ 847", spicy_rules=True),
            HandType.FIVE_OF_A_KIND,
        ),
        (
            Hand.from_input_line("T55J5 847", spicy_rules=True),
            HandType.FOUR_OF_A_KIND,
        ),
        (
            Hand.from_input_line("QQQJA 847", spicy_rules=True),
            HandType.FOUR_OF_A_KIND,
        ),
        (
            Hand.from_input_line("QQJJA 847", spicy_rules=True),
            HandType.FOUR_OF_A_KIND,
        ),
        (
            Hand.from_input_line("JQJJA 847", spicy_rules=True),
            HandType.FOUR_OF_A_KIND,
        ),
        (
            Hand.from_input_line("JJJJA 847", spicy_rules=True),
            HandType.FIVE_OF_A_KIND,
        ),
        (
            Hand.from_input_line("KTJJT 847", spicy_rules=True),
            HandType.FOUR_OF_A_KIND,
        ),
        (
            Hand.from_input_line("J2382 26", spicy_rules=True),
            HandType.THREE_OF_A_KIND,
        ),
        (
            Hand.from_input_line("J2332 26", spicy_rules=True),
            HandType.FULL_HOUSE,
        ),
        (
            Hand.from_input_line("JJ432 26", spicy_rules=True),
            HandType.THREE_OF_A_KIND,
        ),
    ],
)
def test_hand_type_can_be_computed_from_hand(hand, expected_hand_type):
    assert (
        HandType.from_hand(hand=hand, spicy_rules=True) == expected_hand_type
    )


def test_hands_can_be_ordered_with_jokers():
    hands = [FOUR_OF_A_KIND_2, FOUR_OF_A_KIND_1, FOUR_OF_A_KIND_3]
    expected_order = [FOUR_OF_A_KIND_1, FOUR_OF_A_KIND_2, FOUR_OF_A_KIND_3]
    assert sorted(hands) == expected_order


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day7")) == 5905
