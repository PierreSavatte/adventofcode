from dataclasses import dataclass


@dataclass
class Card:
    number: int
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

    def compute_nb_match(self):
        return sum(
            1
            for number in self.numbers_you_have
            if number in self.winning_numbers
        )

    def __hash__(self):
        return self.number


def parse_numbers_list(numbers_txt: str) -> list[int]:
    return [int(number) for number in numbers_txt.split()]


def parse_card_number(card_and_number: str) -> int:
    # expected input = "Card 4"
    return int(card_and_number.split()[1].strip())


def parse_input(data: str) -> list[Card]:
    cards = []
    for line in data.split("\n"):
        card_and_number, numbers = line.split(":")
        winning_numbers_txt, numbers_you_have_txt = numbers.split("|")
        card = Card(
            number=parse_card_number(card_and_number),
            winning_numbers=parse_numbers_list(winning_numbers_txt),
            numbers_you_have=parse_numbers_list(numbers_you_have_txt),
        )
        cards.append(card)
    return cards
