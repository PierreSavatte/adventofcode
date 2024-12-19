from _2024.day19 import (
    AVAILABLE_TOWELS,
    PATTERNS,
    ImpossiblePattern,
    construct_pattern,
    parse_input,
)
from _2024.load_input import load_input


def compute_solution(
    available_towels: AVAILABLE_TOWELS, patterns: PATTERNS
) -> int:
    constructible_patterns = 0
    for pattern in patterns:
        try:
            construct_pattern(pattern, available_towels)
        except ImpossiblePattern:
            continue
        else:
            constructible_patterns += 1
    return constructible_patterns


if __name__ == "__main__":
    input_data = load_input(19)
    available_towels, patterns = parse_input(input_data)
    print(compute_solution(available_towels, patterns))
