from _2023.day7 import parse_input

from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    hands = parse_input(data)

    sorted_hands = sorted(hands)

    winnings = 0
    for rank, hand in enumerate(sorted_hands, start=1):
        winnings += hand.bid * rank

    return winnings


if __name__ == "__main__":
    print(compute_solution(load_input(7)))
