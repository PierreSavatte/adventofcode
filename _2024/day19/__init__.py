TOWEL = str
AVAILABLE_TOWELS = list[TOWEL]
PATTERN = str
PATTERNS = list[PATTERN]


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
) -> list[TOWEL]:
    if pattern == "":
        return []
    
    pattern = pattern[:]
    towels_used = []
    for i in range(len(pattern) + 1, 0, -1):
        pattern_part = pattern[:i]
        if pattern_part in available_towels:
            towels_used.append(pattern_part)
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
