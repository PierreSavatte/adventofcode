from _2024.day1 import parse_input, sort
from _2024.load_input import load_input


def get_distance_between_values(a: int, b: int) -> int:
    return abs(b - a)


def get_distance_between_lists(list_a: list[int], list_b: list[int]):
    return sum(
        get_distance_between_values(a, b)
        for a, b in zip(sort(list_a), sort(list_b))
    )


def main():
    input_data = load_input(1)
    lists = parse_input(input_data)
    print(get_distance_between_lists(*lists))


if __name__ == "__main__":
    main()
