from _2024.day10 import (
    MAP,
    POSITION,
    HikingTrail,
    get_neighbors,
    get_trail_destinations,
    get_trailheads,
    parse_input,
)
from _2024.load_input import load_input


def compute_hiking_trails(map: MAP) -> list[HikingTrail]:
    from _2024.day10.a_star import a_star

    hiking_trails = []

    trail_destinations = get_trail_destinations(map)
    trailheads = get_trailheads(map)
    for trailhead in trailheads:
        for trail_destination in trail_destinations:
            try:
                hiking_trail = a_star(
                    map, get_neighbors, trailhead, trail_destination
                )
            except RuntimeError:
                continue
            hiking_trails.append(HikingTrail(positions=hiking_trail))

    return hiking_trails


def get_trailhead_score(
    trailhead: POSITION, hiking_trails: list[HikingTrail]
) -> int:
    score = 0
    for hiking_trail in hiking_trails:
        trailhead_of_hiking_trail = hiking_trail.positions[0]
        if trailhead_of_hiking_trail == trailhead:
            score += 1
    return score


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
