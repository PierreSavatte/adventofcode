from _2024.day10 import (
    MAP,
    POSITION,
    HikingTrail,
    get_neighbors,
    get_trail_destinations,
    get_trailheads,
    parse_input,
)
from _2024.day10.a_star import PATH
from _2024.load_input import load_input


def find_paths(map, start_position, end_position):
    if start_position == end_position:
        return [[end_position]]

    paths = []
    for neighbors in get_neighbors(map, start_position):
        for path in find_paths(
            map=map, start_position=neighbors, end_position=end_position
        ):
            paths.append([start_position, *path])

    return paths


def compute_all_hiking_trails(map: MAP) -> list[HikingTrail]:
    hiking_trails: list[HikingTrail] = []

    trail_destinations = get_trail_destinations(map)
    trailheads = get_trailheads(map)
    for trailhead in trailheads:
        for trail_destination in trail_destinations:
            try:
                paths: list[PATH] = find_paths(
                    map=map,
                    start_position=trailhead,
                    end_position=trail_destination,
                )
            except RuntimeError:
                continue
            for path in paths:
                hiking_trails.append(HikingTrail(positions=path))

    return hiking_trails


def get_trailhead_rating(
    trailhead: POSITION, hiking_trails: list[HikingTrail]
) -> int:
    trailhead_rating = 0
    for hiking_trail in hiking_trails:
        hiking_trail_trailhead = hiking_trail.positions[0]
        if hiking_trail_trailhead == trailhead:
            trailhead_rating += 1
    return trailhead_rating


def compute_solution(map: MAP) -> int:
    trailheads = get_trailheads(map)
    hiking_trails = compute_all_hiking_trails(map)

    solution = 0
    for trailhead in trailheads:
        trailhead_rating = get_trailhead_rating(trailhead, hiking_trails)
        solution += trailhead_rating

    return solution


def main():
    input_data = load_input(10)
    map = parse_input(input_data)
    print(compute_solution(map))


if __name__ == "__main__":
    main()
