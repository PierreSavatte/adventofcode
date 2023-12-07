from dataclasses import dataclass
from enum import Enum, auto
from collections import defaultdict

CARD_ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARD_ORDER_SPICY_RULES = [
    "A",
    "K",
    "Q",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "J",
]


def list_has_distinct_items(l: list[int], items: list[int]) -> bool:
    l = l.copy()
    for item in items:
        try:
            index = l.index(item)
        except ValueError:
            return False
        l.pop(index)
    return True


class HandType(Enum):
    FIVE_OF_A_KIND = auto()
    FOUR_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    THREE_OF_A_KIND = auto()
    TWO_PAIR = auto()
    ONE_PAIR = auto()
    HIGH_CARD = auto()

    @classmethod
    def _from_hand_classic_rules(cls, hand: "Hand") -> "HandType":
        groups = hand.group()
        values = list(groups.values())
        if 5 in values:
            return HandType.FIVE_OF_A_KIND
        if 4 in values:
            return HandType.FOUR_OF_A_KIND
        if list_has_distinct_items(values, [3, 2]):
            return HandType.FULL_HOUSE
        if 3 in values:
            return HandType.THREE_OF_A_KIND
        if list_has_distinct_items(values, [2, 2]):
            return HandType.TWO_PAIR
        if 2 in values:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    @classmethod
    def _from_hand_spicy_rules(cls, hand: "Hand") -> "HandType":
        groups = hand.group()
        try:
            nb_jokers = groups[Card(face_value="J", spicy_rules=True)]
        except KeyError:
            nb_jokers = 0

        values = list(groups.values())
        if 5 - nb_jokers in values:
            return HandType.FIVE_OF_A_KIND
        if 4 - nb_jokers in values:
            return HandType.FOUR_OF_A_KIND
        if list_has_distinct_items(values, [3 - nb_jokers, 2]):
            return HandType.FULL_HOUSE
        if 3 - nb_jokers in values:
            return HandType.THREE_OF_A_KIND
        if list_has_distinct_items(values, [2 - nb_jokers, 2]):
            return HandType.TWO_PAIR
        if 2 - nb_jokers in values:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    @classmethod
    def from_hand(cls, hand: "Hand", spicy_rules: bool = False) -> "HandType":
        if spicy_rules:
            return cls._from_hand_spicy_rules(hand)
        else:
            return cls._from_hand_classic_rules(hand)


def get_card_index(face_value: str, spicy_rules: bool) -> int:
    if spicy_rules:
        return CARD_ORDER_SPICY_RULES.index(face_value)
    else:
        return CARD_ORDER.index(face_value)


@dataclass
class Card:
    face_value: str
    spicy_rules: bool = False

    def __gt__(self, other):
        self_index = get_card_index(
            self.face_value, spicy_rules=self.spicy_rules
        )
        other_index = get_card_index(
            other.face_value, spicy_rules=self.spicy_rules
        )
        return self_index < other_index

    def __eq__(self, other):
        self_index = get_card_index(
            self.face_value, spicy_rules=self.spicy_rules
        )
        other_index = get_card_index(
            other.face_value, spicy_rules=self.spicy_rules
        )
        return self_index == other_index

    def __lt__(self, other):
        return not self > other and self != other

    def __hash__(self):
        return get_card_index(self.face_value, spicy_rules=self.spicy_rules)


@dataclass
class Hand:
    cards: list[Card]
    bid: int = 0
    spicy_rules: bool = False

    @property
    def hand_type(self) -> HandType:
        return HandType.from_hand(self, spicy_rules=self.spicy_rules)

    def __gt__(self, other):
        self_hand_type = self.hand_type
        other_hand_type = other.hand_type
        if self_hand_type != other_hand_type:
            return self_hand_type.value < other_hand_type.value

        for self_card, other_card in zip(self.cards, other.cards):
            if self_card == other_card:
                continue
            return self_card > other_card

    def __lt__(self, other):
        return not self > other and self != other

    def group(self):
        values_dict = defaultdict(int)
        for card in self.cards:
            values_dict[card] += 1
        return dict(values_dict)

    @classmethod
    def from_input_line(
        cls, input_line: str, spicy_rules: bool = False
    ) -> "Hand":
        cards_txt, bid_str = input_line.split()
        return Hand(
            cards=[
                Card(card_str, spicy_rules=spicy_rules)
                for card_str in cards_txt
            ],
            bid=int(bid_str),
            spicy_rules=spicy_rules,
        )

    def __repr__(self):
        cards = "".join([card.face_value for card in self.cards])
        bid = self.bid
        hand_type = self.hand_type
        return f"<Hand {cards=} {bid=} {hand_type=}>"


def parse_input(data: str, spicy_rules: bool = False) -> list[Hand]:
    return [
        Hand.from_input_line(line, spicy_rules=spicy_rules)
        for line in data.split("\n")
    ]
