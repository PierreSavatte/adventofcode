from dataclasses import dataclass


@dataclass
class Card:
    winning_numbers: list[int]
    numbers_you_have: list[int]

    def compute_points(self):
        points = 0
        for number in self.numbers_you_have:
            if number in self.winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        return points


def parse_numbers_list(numbers_txt: str) -> list[int]:
    return [int(number) for number in numbers_txt.split()]


def parse_input(data: str) -> list[Card]:
    cards = []
    for line in data.split("\n"):
        _, numbers = line.split(":")
        winning_numbers_txt, numbers_you_have_txt = numbers.split("|")
        card = Card(
            winning_numbers=parse_numbers_list(winning_numbers_txt),
            numbers_you_have=parse_numbers_list(numbers_you_have_txt),
        )
        cards.append(card)
    return cards
