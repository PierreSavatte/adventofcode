import re

from _2024.day3 import compute_solution, parse_input
from _2024.load_input import load_input

PART_TO_REMOVE_REGEX = r"don't\(\).*?do\(\)"

END_OF_STRING_WITH_DONT = r"don't\(\).*?$"


def remove_ignored_part_of_input(data: str) -> str:
    data = data.strip()
    split_data = re.split(PART_TO_REMOVE_REGEX, data)
    new_data = "".join(split_data)

    split_data = re.split(END_OF_STRING_WITH_DONT, new_data)

    return "".join(split_data)


if __name__ == "__main__":
    input_data = load_input(3)
    groups = parse_input(remove_ignored_part_of_input(input_data))
    print(compute_solution(groups))
