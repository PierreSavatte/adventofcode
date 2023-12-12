import re


def smart_split(string: str, split_char: str = r"\.") -> list[str]:
    return [group for group in re.split(fr"{split_char}+", string) if group]


def is_composed_only_of_springs(string: str):
    return all(c == "#" for c in string)


def count_existing_groups(springs: str) -> list[int]:
    return [
        len(group)
        for group in smart_split(springs)
        if is_composed_only_of_springs(group)
    ]


def make_arrangements(springs: str):
    if springs == "":
        return [""]
    if springs in [".", "#"]:
        return [springs]
    if springs == "?":
        return [".", "#"]
    else:
        first_char_options = make_arrangements(springs[0])
        other_chars_options = make_arrangements(springs[1:])
        return [
            f"{i}{rest}"
            for i in first_char_options
            for rest in other_chars_options
        ]


def compute_arrangements(input_line: str) -> list[str]:
    springs, groups_txt = input_line.split(" ")
    groups = [int(group) for group in groups_txt.split(",")]

    possible_arrangements = []
    for arrangement in make_arrangements(springs):
        if count_existing_groups(arrangement) == groups:
            possible_arrangements.append(arrangement)
    return possible_arrangements


def compute_total_arrangements(input_line: str) -> int:
    return len(compute_arrangements(input_line))
