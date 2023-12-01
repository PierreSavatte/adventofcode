from typing import Optional

from _2023.load_input import load_input

MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def has_digit_spelled_out_in_string(string: str) -> Optional[str]:
    for accepted_sub_string, digit in MAPPING.items():
        if accepted_sub_string in string:
            return str(digit)
    return None


def _get_digit(character: str, already_parsed: str) -> Optional[str]:
    # Handle digit
    if character.isdecimal():
        return character

    # Handle spelled out digit
    digit = has_digit_spelled_out_in_string(already_parsed)
    if digit is not None:
        return digit


def get_first_integer(line: str) -> str:
    i = 0
    already_parsed = ""
    while i < len(line):
        character = line[i]
        already_parsed = f"{already_parsed}{character}"

        digit = _get_digit(character, already_parsed)
        if digit:
            return digit

        i += 1


def get_last_integer(line: str) -> str:
    i = len(line) - 1
    already_parsed = ""
    while i >= 0:
        character = line[i]
        already_parsed = f"{character}{already_parsed}"

        digit = _get_digit(character, already_parsed)
        if digit:
            return digit

        i -= 1


def parse_line(line: str) -> int:
    first = get_first_integer(line)
    last = get_last_integer(line)
    return int("".join([first, last]))


def compute_answer(data: str):
    return sum(parse_line(line) for line in data.split("\n"))


if __name__ == "__main__":
    print(compute_answer(load_input(1)))
