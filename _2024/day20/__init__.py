from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Optional

from _2024.day10.a_star import Direction, a_star, euclidean_distance

POSITION = tuple[int, int]


@dataclass
class Map:
    start: POSITION
    end: POSITION
    cells: list[str]

    @property
    def size(self) -> int:
        return len(self.cells)

    def in_map(self, position: POSITION) -> bool:
        x, y = position
        return 0 <= x < self.size and 0 <= y < self.size

    def get_neighbors(
        self, map: Any, current: POSITION, direction: Direction
    ) -> list[POSITION]:
        x, y = current
        neighbors = []
        for direction in Direction:
            delta_x, delta_y = direction.to_delta_position()
            new_position = x + delta_x, y + delta_y
            character = self.cells[y][x]
            if self.in_map(new_position) and character != "#":
                neighbors.append(new_position)
        return neighbors

    def compute_path(self) -> list[POSITION]:
        return a_star(
            map=self.cells,
            get_neighbors=self.get_neighbors,
            start_position=self.start,
            end_position=self.end,
            distance_function=euclidean_distance,
        )


TIME_SAVED = int
NB_SHORTCUTS = int


def compute_shortcuts(path: list[POSITION]) -> dict[TIME_SAVED, NB_SHORTCUTS]:
    shortcuts = defaultdict(int)
    for i, position in enumerate(path):
        rest_of_the_path = path[i + 1 :]
        x, y = position
        for direction in Direction:
            delta_x, delta_y = direction.to_delta_position()
            new_position = x + 2 * delta_x, y + 2 * delta_y
            intermediary_position = (x + delta_x, y + delta_y)
            if (
                new_position in rest_of_the_path
                and intermediary_position not in rest_of_the_path
            ):
                new_index = path.index(new_position)
                time_saved = new_index - i - 2
                shortcuts[time_saved] += 1
    return dict(shortcuts)


def parse_input(data: str) -> Map:
    data = data.strip("\n")
    cells = []
    start = None
    end = None
    for y, line in enumerate(data.split("\n")):
        new_line = ""
        for x, character in enumerate(line):
            if character == "S":
                start = (x, y)
                character = "."
            elif character == "E":
                end = (x, y)
                character = "."

            new_line += character
        cells.append(new_line)

    if not start:
        raise RuntimeError("Didn't find start position in input.")
    if not end:
        raise RuntimeError("Didn't find end position in input.")

    return Map(start=start, end=end, cells=cells)
