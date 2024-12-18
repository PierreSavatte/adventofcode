import math
from queue import PriorityQueue

from _2024.day10.a_star import Direction, euclidean_distance

POSITION = tuple[int, int]
LIST_OF_OBSTACLES = list[POSITION]
PATH = list[POSITION]


class Map:
    def __init__(
        self,
        map_size: int,
        obstacles: LIST_OF_OBSTACLES,
        current_fallen_bytes_number: int,
    ):
        self.map_size = map_size
        self.start_position = (0, 0)
        self.end_position = (map_size, map_size)
        self.obstacles = obstacles
        self.current_fallen_bytes_number = current_fallen_bytes_number

    def in_map(self, position: POSITION) -> bool:
        x, y = position
        return 0 <= x <= self.map_size and 0 <= y <= self.map_size

    @property
    def current_obstacles(self):
        return self.obstacles[: self.current_fallen_bytes_number]

    def get_neighbors(self, current: POSITION) -> list[POSITION]:
        x, y = current
        neighbors = []
        for direction in Direction:
            delta_x, delta_y = direction.to_delta_position()
            new_position = x + delta_x, y + delta_y
            if (
                self.in_map(new_position)
                and new_position not in self.current_obstacles
            ):
                neighbors.append(new_position)

        return neighbors

    def get_path(self) -> PATH:
        open_set = PriorityQueue()
        open_set.put(item=(0, self.start_position, [self.start_position]))

        g_score = {self.start_position: 0}

        while not open_set.empty():
            current_g_score, current, path = open_set.get()

            if current == self.end_position:
                return path

            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                distance_current_neighbor = euclidean_distance(
                    current, neighbor
                )
                tentative_g_score = current_g_score + distance_current_neighbor

                already_existing_g_score = g_score.get(neighbor, math.inf)
                if tentative_g_score <= already_existing_g_score:
                    g_score[neighbor] = tentative_g_score

                    already_in_open = any(
                        neighbor in item for item in open_set.queue
                    )
                    if not already_in_open:
                        open_set.put(
                            item=(
                                tentative_g_score,
                                neighbor,
                                [*path, neighbor],
                            )
                        )
        raise RuntimeError("Was not able to find a path")

    def plot(self) -> str:
        map = []
        for y in range(self.map_size + 1):
            line = []
            for x in range(self.map_size + 1):
                if (x, y) in self.current_obstacles:
                    character = "#"
                else:
                    character = "."
                line.append(character)
            map.append(line)

        plotted_map = []
        for line in map:
            plotted_map.append("".join(line))

        return "\n".join(plotted_map)

    def __eq__(self, other: "Map") -> bool:
        if not isinstance(other, Map):
            raise NotImplementedError()

        return (
            self.map_size == other.map_size
            and self.obstacles == other.obstacles
            and self.current_fallen_bytes_number
            == other.current_fallen_bytes_number
        )


def parse_input(
    data: str, map_size: int, current_fallen_bytes_number: int
) -> Map:
    data = data.strip("\n")
    obstacles: list[POSITION] = [  # type:ignore
        tuple(map(int, line.split(","))) for line in data.split("\n")
    ]
    return Map(
        map_size=map_size,
        current_fallen_bytes_number=current_fallen_bytes_number,
        obstacles=obstacles,
    )
