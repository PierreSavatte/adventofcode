from _2023.day13 import parse_patterns, Pattern
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    total = 0
    for pattern_raw in parse_patterns(data):
        pattern = Pattern.from_data(data=pattern_raw, should_fix_smudge=True)
        total += pattern.reflection.summarize()
    return total


if __name__ == "__main__":
    # 8472 < solution < 30209
    # 31102 incorrect
    print(compute_solution(load_input(13)))
