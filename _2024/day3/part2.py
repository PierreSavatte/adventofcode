import re

from _2024.day3 import compute_solution, parse_input
from _2024.load_input import load_input

PART_TO_REMOVE_REGEX = r"don't\(\).*?do\(\)"

END_OF_STRING_WITH_DONT = r"don't\(\)(?!.*don't\(\)).*\Z"


def remove_ignored_part_of_input(data: str) -> str:
    data = data.strip()
    data = re.sub(PART_TO_REMOVE_REGEX, "", data)

    match = re.search(END_OF_STRING_WITH_DONT, data)
    if match:
        end_with_dont = match.group()
        if not "do()" in end_with_dont:
            data = re.sub(END_OF_STRING_WITH_DONT, "", data)

    return data


if __name__ == "__main__":
    input_data = load_input(3)
    new_input_data = remove_ignored_part_of_input(input_data)
    groups = parse_input(new_input_data)
    print(compute_solution(groups))
