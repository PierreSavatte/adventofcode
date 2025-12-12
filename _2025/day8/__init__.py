import math
from dataclasses import dataclass

import tqdm


@dataclass
class Position:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


@dataclass
class BasePlayground:
    def __init__(self, positions: list[Position]):
        self.positions = positions

        self.groups: list[set[Position]] = [
            {position} for position in self.positions
        ]
        self.distances = {
            compute_distance(a, b): (a, b)
            for i, a in enumerate(positions)
            for b in positions[i + 1 :]
        }

    def pop_closest_boxes(self) -> tuple[Position, Position]:
        min_distance = min(self.distances.keys())
        boxes = self.distances.pop(min_distance)
        return boxes

    def update_groups(self, boxes_to_join: tuple[Position, Position]) -> bool:
        """Returns if a and b are not already in the same group"""
        a, b = boxes_to_join

        index_a = None
        index_b = None
        for i, group in enumerate(self.groups):
            if a in group and b in group:
                return False
            if a in group:
                index_a = i
            if b in group:
                index_b = i

        if index_a is None or index_b is None:
            raise RuntimeError(
                "Hasn't found a or b in groups. Something wrong happened."
            )

        group_with_b_in_it = self.groups[index_b]
        self.groups[index_a].update(group_with_b_in_it)
        self.groups.pop(index_b)

        return True

    def make_next_connection(self):
        closest_boxes = self.pop_closest_boxes()
        self.update_groups(closest_boxes)

    def get_group_sizes(self) -> list[int]:
        return sorted([len(group) for group in self.groups], reverse=True)

    def get_last_connection_pair(self) -> tuple[Position, Position]:
        progress_bar = tqdm.tqdm(total=len(self.positions))
        while len(self.groups) > 1:
            closest_boxes = self.pop_closest_boxes()
            has_linked_boxes = self.update_groups(closest_boxes)

            if has_linked_boxes:
                progress_bar.update()
        return closest_boxes

    @classmethod
    def from_input(cls, input: str) -> "BasePlayground":
        positions = []
        for line in input.strip().splitlines():
            position = Position(*map(int, line.split(",")))
            positions.append(position)
        return cls(positions)


def compute_distance(a: Position, b: Position) -> float:
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)
