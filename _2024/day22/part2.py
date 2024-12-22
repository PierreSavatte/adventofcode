from collections import defaultdict

from _2024.day22 import generate_next_secret_number, parse_input
from _2024.load_input import load_input

SECRET_NUMBER = int
PRICE_DIFF_SEQUENCE = tuple[int, int, int, int]
PRICE = int


def get_price(secret_number: int) -> int:
    return int(str(secret_number)[-1])


def get_price_differences(sequence: list[int]) -> list[int]:
    price_differences = []
    for a, b in zip(sequence, sequence[1:]):
        price_a = get_price(a)
        price_b = get_price(b)
        price_differences.append(price_b - price_a)
    return price_differences


def get_all_secret_numbers(secret_number: int, n: int = 2000) -> list[int]:
    secret_numbers = []
    for i in range(n):
        secret_numbers.append(secret_number)
        secret_number = generate_next_secret_number(secret_number)
    return [secret_number, *secret_numbers]


def get_all_sequences_price_mapping(
    secret_numbers: list[int],
) -> dict[SECRET_NUMBER, dict[PRICE_DIFF_SEQUENCE, PRICE]]:
    all_sequence_price_mapping = {}
    for secret_number in secret_numbers:
        secret_numbers_sequence = get_all_secret_numbers(secret_number)
        price_differences = get_price_differences(secret_numbers_sequence)
        sequence_price_mapping = {}
        for i in range(len(price_differences) - 5):
            a, b, c, d = price_differences[i : i + 4]
            sequence = (a, b, c, d)
            next_price = get_price(secret_numbers_sequence[4 + i])
            if sequence not in sequence_price_mapping:
                sequence_price_mapping[sequence] = next_price
        all_sequence_price_mapping[secret_number] = sequence_price_mapping
    return all_sequence_price_mapping


def get_best_sequence(
    secret_numbers: list[int],
) -> tuple[PRICE_DIFF_SEQUENCE, PRICE]:
    all_sequence_price_mapping = get_all_sequences_price_mapping(
        secret_numbers
    )
    sequences_prices = defaultdict(int)
    for secret_number in secret_numbers:
        sequence_price_mapping = all_sequence_price_mapping[secret_number]
        for sequence, price in sequence_price_mapping.items():
            sequences_prices[sequence] += price

    sorted_sequences = sorted(
        sequences_prices.items(), key=lambda x: x[1], reverse=True
    )
    best_item = sorted_sequences[0]
    return best_item


def compute_solution(secret_numbers: list[int]) -> int:
    sequence, price = get_best_sequence(secret_numbers)
    return price


def main():
    input_data = load_input(22)
    secret_numbers = parse_input(input_data)
    print(compute_solution(secret_numbers))


if __name__ == "__main__":
    main()
