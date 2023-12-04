from dataclasses import dataclass

from _2023.day4 import Card, parse_input
from _2023.load_input import load_input


@dataclass
class Deck:
    mapping: dict[Card, int]

    @classmethod
    def from_cards(cls, cards: list[Card]) -> "Deck":
        copies = {card: 1 for card in cards}
        card_index = 0
        while card_index < len(cards):
            card = cards[card_index]
            nb_match = card.compute_nb_match()
            nb_copies = copies[card]
            for i in range(nb_match):
                new_card_index = card_index + 1 + i
                if new_card_index > len(cards):
                    # Cards will never make you copy a card past
                    # the end of the table
                    break
                new_card = cards[new_card_index]
                copies[new_card] += nb_copies

            card_index += 1

        mapping = {
            card.number: nb_copies for card, nb_copies in copies.items()
        }
        return Deck(mapping=mapping)


def compute_solution(data: str) -> int:
    cards = parse_input(data)
    deck = Deck.from_cards(cards)
    return sum(deck.mapping.values())


if __name__ == "__main__":
    print(compute_solution(load_input(4)))
