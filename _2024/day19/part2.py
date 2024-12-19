from _2024.day19 import (
    AVAILABLE_TOWELS,
    PATTERNS,
    ImpossiblePattern,
    construct_all_arrangements,
    parse_input,
)
from _2024.load_input import load_input
from tqdm import tqdm


def compute_solution(
    available_towels: AVAILABLE_TOWELS, patterns: PATTERNS
) -> int:
    solution = 0
    available_towels = tuple(available_towels)
    progress_bar = tqdm(total=len(patterns))
    for pattern in patterns:
        try:
            arrangements = construct_all_arrangements(
                pattern, available_towels
            )
        except ImpossiblePattern:
            pass
        else:
            solution += arrangements
        progress_bar.update()
    progress_bar.close()
    return solution


if __name__ == "__main__":
    input_data = load_input(19)
    available_towels, patterns = parse_input(input_data)
    print(compute_solution(available_towels, patterns))
