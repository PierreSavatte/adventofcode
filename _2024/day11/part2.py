from functools import cache

from _2024.day11 import parse_input
from _2024.load_input import load_input


@cache
def fast_change_stone(stone: int, nb_change: int) -> int:
    if nb_change == 0:
        return 1

    new_nb_change = nb_change - 1

    if stone == 0:
        return fast_change_stone(1, nb_change=new_nb_change)

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        i = len(stone_str) // 2
        a, b = stone_str[:i], stone_str[i:]
        return fast_change_stone(
            int(a), nb_change=new_nb_change
        ) + fast_change_stone(int(b), nb_change=new_nb_change)

    new_stone = stone * 2024
    return fast_change_stone(new_stone, nb_change=new_nb_change)


def fast_change(stones: list[int], nb_change: int) -> int:
    total = 0
    for stone in stones:
        total += fast_change_stone(stone, nb_change)
    return total


def compute_solution(stones: list[int], nb_change: int) -> int:
    return fast_change(stones, nb_change)


def main():
    input_data = load_input(11)
    stones = parse_input(input_data)
    print(compute_solution(stones, nb_change=75))


if __name__ == "__main__":
    main()
