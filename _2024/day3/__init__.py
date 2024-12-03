import re

REGEX = r"mul\((\d+),(\d+)\)"


def parse_input(data: str):
    data = data.strip()
    match = re.findall(REGEX, data)
    return [(int(a), int(b)) for a, b in match]


def compute_solution(groups: list[tuple[int, int]]) -> int:
    return sum(map(lambda t: t[0] * t[1], groups))
