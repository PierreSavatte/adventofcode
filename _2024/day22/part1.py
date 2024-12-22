from _2024.day22 import generate_next_secret_number, parse_input
from _2024.load_input import load_input


def get_nth_secret_number(secret_number: int, n: int) -> int:
    for i in range(n):
        secret_number = generate_next_secret_number(secret_number)
    return secret_number


def compute_solution(secret_numbers: list[int]) -> int:
    return sum(
        get_nth_secret_number(secret_number=secret_number, n=2000)
        for secret_number in secret_numbers
    )


def main():
    input_data = load_input(22)
    secret_numbers = parse_input(input_data)
    print(compute_solution(secret_numbers))


if __name__ == "__main__":
    main()
