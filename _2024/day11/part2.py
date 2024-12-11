from functools import cache

from _2024.day11 import parse_input
from _2024.load_input import load_input


@cache
def change_stone_fast(stone: int, nb_change: int) -> int:
    if nb_change == 0:
        return 1

    new_nb_change = nb_change - 1

    if stone == 0:
        return change_stone_fast(1, nb_change=new_nb_change)

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        i = len(stone_str) // 2
        a, b = stone_str[:i], stone_str[i:]
        return change_stone_fast(
            int(a), nb_change=new_nb_change
        ) + change_stone_fast(int(b), nb_change=new_nb_change)

    new_stone = stone * 2024
    return change_stone_fast(new_stone, nb_change=new_nb_change)


def change_fast(stones: list[int], nb_change: int) -> int:
    total = 0
    for stone in stones:
        total += change_stone_fast(stone, nb_change)
    return total


def compute_solution(stones: list[int], nb_change: int) -> int:
    return change_fast(stones, nb_change)


def main():
    input_data = load_input(11)
    stones = parse_input(input_data)
    print(compute_solution(stones, nb_change=75))


if __name__ == "__main__":
    main()
