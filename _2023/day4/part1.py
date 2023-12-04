from _2023.day4 import parse_input
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    cards = parse_input(data)
    return sum(card.compute_points() for card in cards)


if __name__ == "__main__":
    print(compute_solution(load_input(4)))
