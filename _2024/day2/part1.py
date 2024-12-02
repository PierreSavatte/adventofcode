from _2024.day2 import parse_input
from _2024.load_input import load_input


def are_adjacent_levels_safe(a: int, b: int) -> bool:
    diff = abs(a - b)
    return 1 <= diff <= 3


def _are_levels_strictly_increasing(report: list[int]) -> bool:
    return all(a < b for a, b in zip(report, report[1:]))


def _are_levels_strictly_decreasing(report: list[int]) -> bool:
    return all(a > b for a, b in zip(report, report[1:]))


def are_levels_strictly_monotonic(report: list[int]) -> bool:
    strictly_increasing = _are_levels_strictly_increasing(report)
    strictly_decreasing = _are_levels_strictly_decreasing(report)
    return strictly_increasing or strictly_decreasing


def is_safe(report: list[int]) -> bool:
    all_adjacent_levels_are_safe = all(
        are_adjacent_levels_safe(a, b) for a, b in zip(report, report[1:])
    )
    levels_strictly_are_monotonic = are_levels_strictly_monotonic(report)
    return all_adjacent_levels_are_safe and levels_strictly_are_monotonic


def count_safe_reports(data: str) -> int:
    list_of_reports = parse_input(data)
    return sum(is_safe(report) for report in list_of_reports)


if __name__ == "__main__":
    input_data = load_input(2)
    print(count_safe_reports(input_data))
