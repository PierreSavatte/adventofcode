def are_adjacent_levels_safe(a: int, b: int) -> bool:
    diff = abs(a - b)
    return 1 <= diff <= 3


def _are_levels_strictly_increasing(levels: list[int]) -> bool:
    return all(a < b for a, b in zip(levels, levels[1:]))


def _are_levels_strictly_decreasing(levels: list[int]) -> bool:
    return all(a > b for a, b in zip(levels, levels[1:]))


def are_levels_strictly_monotonic(levels: list[int]) -> bool:
    strictly_increasing = _are_levels_strictly_increasing(levels)
    strictly_decreasing = _are_levels_strictly_decreasing(levels)
    return strictly_increasing or strictly_decreasing


def is_safe(levels: list[int]) -> bool:
    all_adjacent_levels_are_safe = all(
        are_adjacent_levels_safe(a, b) for a, b in zip(levels, levels[1:])
    )
    levels_strictly_are_monotonic = are_levels_strictly_monotonic(levels)
    return all_adjacent_levels_are_safe and levels_strictly_are_monotonic


def parse_input(data: str) -> list[list[int]]:
    data = data.strip("\n")
    return [list(map(int, line.split())) for line in data.split("\n")]
