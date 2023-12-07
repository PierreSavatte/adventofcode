import pytest

from _2023.day7 import Card, Hand, HandType, parse_input
from _2023.day7.part1 import compute_solution

A = Card(face_value="A")
K = Card(face_value="K")
Q = Card(face_value="Q")
J = Card(face_value="J")
T = Card(face_value="T")
_9 = Card(face_value="9")
_8 = Card(face_value="8")
_7 = Card(face_value="7")
_6 = Card(face_value="6")
_5 = Card(face_value="5")
_4 = Card(face_value="4")
_3 = Card(face_value="3")
_2 = Card(face_value="2")


def test_cards_are_sortable():
    assert A > K > Q > J > T > _9 > _8 > _7 > _6 > _5 > _4 > _3 > _2

    assert _2 < _3 < _4 < _5 < _6 < _7 < _8 < _9 < T < J < Q < K < A

    assert _2 == _2
    assert A == A


FIVE_OF_A_KIND = Hand(cards=[A, A, A, A, A])
FOUR_OF_A_KIND = Hand(cards=[A, A, _8, A, A])
FULL_HOUSE = Hand(cards=[_2, _3, _3, _3, _2])
THREE_OF_A_KIND = Hand(cards=[T, T, T, _9, _8])
TWO_PAIR = Hand(cards=[_2, _3, _4, _3, _2])
ONE_PAIR = Hand(cards=[A, _2, _3, A, _4])
HIGH_CARD = Hand(cards=[_2, _3, _4, _5, _6])


@pytest.mark.parametrize(
    "hand, expected_groups",
    [
        (FIVE_OF_A_KIND, {A: 5}),
        (FOUR_OF_A_KIND, {A: 4, _8: 1}),
        (FULL_HOUSE, {_3: 3, _2: 2}),
        (THREE_OF_A_KIND, {T: 3, _9: 1, _8: 1}),
        (TWO_PAIR, {_4: 1, _3: 2, _2: 2}),
        (ONE_PAIR, {A: 2, _4: 1, _3: 1, _2: 1}),
        (
            HIGH_CARD,
            {_6: 1, _5: 1, _4: 1, _3: 1, _2: 1},
        ),
    ],
)
def test_hand_can_group_cards(hand, expected_groups):
    assert hand.group() == expected_groups


@pytest.mark.parametrize(
    "hand, expected_hand_type",
    [
        (FIVE_OF_A_KIND, HandType.FIVE_OF_A_KIND),
        (FOUR_OF_A_KIND, HandType.FOUR_OF_A_KIND),
        (FULL_HOUSE, HandType.FULL_HOUSE),
        (THREE_OF_A_KIND, HandType.THREE_OF_A_KIND),
        (TWO_PAIR, HandType.TWO_PAIR),
        (ONE_PAIR, HandType.ONE_PAIR),
        (HIGH_CARD, HandType.HIGH_CARD),
    ],
)
def test_hand_type_can_be_computed_from_hand(hand, expected_hand_type):
    assert HandType.from_hand(hand=hand) == expected_hand_type


def test_hand_are_sortable():
    assert (
        FIVE_OF_A_KIND
        > FOUR_OF_A_KIND
        > FULL_HOUSE
        > THREE_OF_A_KIND
        > TWO_PAIR
        > ONE_PAIR
        > HIGH_CARD
    )
    assert (
        HIGH_CARD
        < ONE_PAIR
        < TWO_PAIR
        < THREE_OF_A_KIND
        < FULL_HOUSE
        < FOUR_OF_A_KIND
        < FIVE_OF_A_KIND
    )


def test_same_hand_types_get_sorted_by_card():
    assert Hand(cards=[Q, Q, Q, J, A]) > Hand(cards=[T, _5, _5, J, _5])


def test_hands_can_be_sorted():
    input_hands = [
        HIGH_CARD,
        TWO_PAIR,
        FIVE_OF_A_KIND,
        THREE_OF_A_KIND,
        FOUR_OF_A_KIND,
        ONE_PAIR,
        FULL_HOUSE,
    ]
    expected_output_hands = [
        HIGH_CARD,
        ONE_PAIR,
        TWO_PAIR,
        THREE_OF_A_KIND,
        FULL_HOUSE,
        FOUR_OF_A_KIND,
        FIVE_OF_A_KIND,
    ]

    assert sorted(input_hands) == expected_output_hands


def test_similar_hands_are_sorted_properly():
    hands = [
        Hand(cards=[_2, _6, _5, J, K]),
        Hand(cards=[_2, _5, T, _4, _6]),
        Hand(cards=[_2, A, _5, _7, _3]),
        Hand(cards=[_2, K, _8, _4, J]),
        Hand(cards=[_2, _6, _8, _5, _9]),
    ]
    assert sorted(hands) == [
        Hand(cards=[_2, _5, T, _4, _6]),
        Hand(cards=[_2, _6, _5, J, K]),
        Hand(cards=[_2, _6, _8, _5, _9]),
        Hand(cards=[_2, K, _8, _4, J]),
        Hand(cards=[_2, A, _5, _7, _3]),
    ]


@pytest.mark.parametrize(
    "line, expected_hand",
    [
        ("32T3K 765", Hand(cards=[_3, _2, T, _3, K], bid=765)),
        ("T55J5 684", Hand(cards=[T, _5, _5, J, _5], bid=684)),
        ("KK677 28", Hand(cards=[K, K, _6, _7, _7], bid=28)),
        ("KTJJT 220", Hand(cards=[K, T, J, J, T], bid=220)),
        ("QQQJA 483", Hand(cards=[Q, Q, Q, J, A], bid=483)),
    ],
)
def test_line_can_be_parsed(line, expected_hand):
    assert Hand.from_input_line(line) == expected_hand


def test_input_can_be_parsed(get_data):
    assert parse_input(get_data("test_file_day7")) == [
        Hand(cards=[_3, _2, T, _3, K], bid=765),
        Hand(cards=[T, _5, _5, J, _5], bid=684),
        Hand(cards=[K, K, _6, _7, _7], bid=28),
        Hand(cards=[K, T, J, J, T], bid=220),
        Hand(cards=[Q, Q, Q, J, A], bid=483),
    ]


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day7")) == 6440
