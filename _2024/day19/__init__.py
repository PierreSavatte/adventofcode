from functools import cache

TOWEL = str
AVAILABLE_TOWELS = list[TOWEL]
PATTERN = str
PATTERNS = list[PATTERN]
ARRANGEMENT = list[TOWEL]


class ImpossiblePattern(Exception):
    ...


def parse_input(data: str) -> tuple[AVAILABLE_TOWELS, PATTERNS]:
    data = data.strip("\n")
    available_towels_str, patterns_str = data.split("\n\n")
    available_towels = available_towels_str.split(", ")
    patterns = patterns_str.split("\n")
    return available_towels, patterns


def construct_pattern(
    pattern: PATTERN, available_towels: AVAILABLE_TOWELS
) -> ARRANGEMENT:
    if pattern == "":
        return []

    pattern = pattern[:]
    for i in range(len(pattern) + 1, 0, -1):
        pattern_part = pattern[:i]
        if pattern_part in available_towels:
            try:
                return [
                    pattern_part,
                    *construct_pattern(pattern[i:], available_towels),
                ]
            except ImpossiblePattern:
                continue
    else:
        raise ImpossiblePattern(
            f"The pattern ({pattern=}) (or its rest) cannot "
            f"be built with the {available_towels=}"
        )


@cache
def construct_all_arrangements(
    pattern: PATTERN, available_towels: tuple[TOWEL]
) -> int:
    if len(pattern) == 1:
        if pattern in available_towels:
            return 1

    arrangements = 0
    for i in range(len(pattern), 0, -1):
        pattern_part = pattern[:i]
        pattern_rest = pattern[i:]
        if pattern_part in available_towels:
            if len(pattern_rest) == 0:
                arrangements += 1
                continue
            try:
                sub_arrangements = construct_all_arrangements(
                    pattern_rest, available_towels
                )
            except ImpossiblePattern:
                continue
            else:
                arrangements += sub_arrangements
    if not arrangements:
        raise ImpossiblePattern(
            f"The pattern ({pattern=}) (or its rest) cannot "
            f"be built with the {available_towels=}"
        )
    return arrangements
