from _2024.day11 import change, parse_input
from _2024.load_input import load_input


def compute_solution(stones: list[int], nb_change: int) -> int:
    for i in range(nb_change):
        stones = change(stones)
    return len(stones)


def main():
    input_data = load_input(11)
    stones = parse_input(input_data)
    print(compute_solution(stones, nb_change=25))


if __name__ == "__main__":
    main()
