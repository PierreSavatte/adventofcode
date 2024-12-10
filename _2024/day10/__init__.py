from dataclasses import dataclass

MAP = list[list[int]]
POSITION = tuple[int, int]


def parse_input(data: str) -> MAP:
    data = data.strip("\n")

    map = [[int(char) for char in line] for line in data.split("\n")]

    return map


def _get_positions(map: MAP, lookup_value: int) -> list[POSITION]:
    trailheads = []
    for y, line in enumerate(map):
        for x, cell in enumerate(line):
            if cell == lookup_value:
                trailheads.append((x, y))
    return trailheads


def get_trailheads(map: MAP) -> list[POSITION]:
    return _get_positions(map, lookup_value=0)


def get_trail_destinations(map: MAP) -> list[POSITION]:
    return _get_positions(map, lookup_value=9)


def get_value(map: MAP, position: POSITION) -> int:
    x, y = position
    return map[y][x]


def get_neighbors(map: MAP, position: POSITION) -> list[POSITION]:
    map_size = len(map)
    x, y = position

    neighbors = []
    for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = position
        new_x = x + delta_x
        new_y = y + delta_y
        if not (0 <= new_x < map_size and 0 <= new_y < map_size):
            # Not in the map
            continue

        new_position = (new_x, new_y)
        if get_value(map, new_position) == get_value(map, position) + 1:
            neighbors.append(new_position)
    return neighbors


@dataclass
class HikingTrail:
    positions: list[POSITION]


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
            hiking_trails.append(
                HikingTrail(positions=[trailhead, *hiking_trail])
            )

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
