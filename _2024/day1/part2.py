from _2024.day1 import parse_input, sort
from _2024.load_input import load_input


def get_similarity_increase(value: int, list_to_compare: list[int]) -> int:
    return list_to_compare.count(value) * value


def compute_similarity_score(list_a: list[int], list_b: list[int]) -> int:
    return sum(get_similarity_increase(a, list_b) for a in list_a)


def main():
    input_data = load_input(1)
    lists = parse_input(input_data)
    print(compute_similarity_score(*lists))


if __name__ == "__main__":
    main()
