from _2023.load_input import load_input
from functools import cache


@cache
def compute_arrangements(springs: str, groups: tuple[int]) -> int:
    if not groups:
        if "#" in springs:
            return 0
        else:
            return 1

    if not springs:
        return 0

    current_group = groups[0]
    current_character = springs[0]

    def dot_case():
        return compute_arrangements(springs[1:], groups)

    def hash_case():
        next_characters = springs[:current_group]
        next_characters = next_characters.replace("?", "#")

        if next_characters != "#" * current_group:
            return 0

        if len(springs) == current_group:
            if len(groups) == 1:
                return 1
            else:
                return 0

        if springs[current_group] in "?.":
            return compute_arrangements(
                springs[current_group + 1 :], groups[1:]
            )

        return 0

    if current_character == ".":
        return dot_case()
    elif current_character == "#":
        return hash_case()
    elif current_character == "?":
        return dot_case() + hash_case()

    raise RuntimeError("Got an error")


def compute_unfolded_arrangements(line: str) -> int:
    springs, groups_txt = line.split(" ")
    groups = [int(group) for group in groups_txt.split(",")]

    unfolded_springs = "?".join([springs] * 5)
    unfolded_groups = tuple(groups * 5)

    return compute_arrangements(unfolded_springs, unfolded_groups)


def compute_solution(data: str) -> int:
    total_possible_arrangements = 0
    for line in data.splitlines():
        total_possible_arrangements += compute_unfolded_arrangements(line)
    return total_possible_arrangements


if __name__ == "__main__":
    print(compute_solution(load_input(12)))
