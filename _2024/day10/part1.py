from _2024.day10 import (
    MAP,
    compute_hiking_trails,
    get_trailhead_score,
    get_trailheads,
    parse_input,
)
from _2024.load_input import load_input


def compute_solution(map: MAP) -> int:
    trailheads = get_trailheads(map)
    hiking_trails = compute_hiking_trails(map)
    solution = 0
    for trailhead in trailheads:
        solution += get_trailhead_score(trailhead, hiking_trails)

    return solution


def main():
    input_data = load_input(10)
    map = parse_input(input_data)
    print(compute_solution(map))


if __name__ == "__main__":
    main()
