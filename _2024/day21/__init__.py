from abc import ABC
from functools import cache
from typing import Any

from _2024.day10.a_star import Direction, a_star, euclidean_distance
from tqdm import tqdm

POSITION = tuple[int, int]
BUTTON = str
TYPING_SEQUENCE = str


@cache
def get_typing_sequence(path: tuple[POSITION]) -> tuple[str]:
    typing_sequence = []
    for a, b in zip(path, path[1:]):
        typing_sequence.append(Direction.from_two_points(a, b).to_str())
    return tuple(typing_sequence)


class KeyPad(ABC):
    buttons: dict[BUTTON, POSITION]

    def __init__(self):
        self.cached_paths = {}
        self.cached_neighbors = {}
        self.cached_typing_sequences = {}

    def get_neighbors(
        self, map: Any, current: POSITION, direction: Direction
    ) -> list[POSITION]:
        if current in self.cached_neighbors:
            return self.cached_neighbors[current]

        x, y = current
        neighbors = []
        for delta_x, delta_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            neighbor = x + delta_x, y + delta_y
            if neighbor in self.buttons.values():
                neighbors.append(neighbor)

        self.cached_neighbors[current] = neighbors

        return neighbors

    def get_paths(
        self, start: POSITION, end: POSITION
    ) -> list[list[POSITION]]:
        if (start, end) in self.cached_paths:
            return self.cached_paths[(start, end)]

        paths = a_star(
            map=None,
            get_neighbors=self.get_neighbors,
            start_position=start,
            end_position=end,
            distance_function=euclidean_distance,
            multiple_optimal_paths=True,
        )
        self.cached_paths[(start, end)] = paths
        return paths

    @property
    def start_position(self) -> POSITION:
        return self.buttons["A"]

    def _compute_shortest_typing_sequences(
        self, buttons_to_press: str, pointer: POSITION
    ) -> list[list[BUTTON]]:
        if buttons_to_press == "":
            return [[]]

        key = (pointer, buttons_to_press)
        if key in self.cached_typing_sequences:
            return self.cached_typing_sequences[key]

        button = buttons_to_press[0]
        rest_of_the_buttons = buttons_to_press[1:]
        next_position = self.buttons[button]
        typing_sequences = []
        for path in self.get_paths(pointer, next_position):
            direction_list = list(get_typing_sequence(tuple(path)))

            for sub_typing_sequence in self._compute_shortest_typing_sequences(
                rest_of_the_buttons, next_position
            ):
                typing_sequences.append(
                    [*direction_list, "A", *sub_typing_sequence]
                )

        self.cached_typing_sequences[key] = typing_sequences

        return typing_sequences

    def compute_shortest_typing_sequences(
        self, typing_sequence: str
    ) -> set[TYPING_SEQUENCE]:
        pointer = self.start_position
        typing_sequences = self._compute_shortest_typing_sequences(
            typing_sequence, pointer
        )
        return {
            "".join(typing_sequence) for typing_sequence in typing_sequences
        }

    def compute_typing_sequences_from_typing_sequences(
        self, typing_sequences: set[TYPING_SEQUENCE]
    ) -> set[TYPING_SEQUENCE]:
        new_typing_sequences = set()
        progress_bar = tqdm(total=len(typing_sequences))
        for typing_sequence in typing_sequences:
            new_typing_sequences.update(
                self.compute_shortest_typing_sequences(typing_sequence)
            )
            progress_bar.update()
        progress_bar.close()
        return new_typing_sequences


class DoorKeyPad(KeyPad):
    buttons = {
        "9": (2, 0),
        "8": (1, 0),
        "7": (0, 0),
        "6": (2, 1),
        "5": (1, 1),
        "4": (0, 1),
        "3": (2, 2),
        "2": (1, 2),
        "1": (0, 2),
        "0": (1, 3),
        "A": (2, 3),
    }


class DirectionalKeyPad(KeyPad):
    buttons = {
        "^": (1, 0),
        "A": (2, 0),
        "<": (0, 1),
        "v": (1, 1),
        ">": (2, 1),
    }


def compute_complexity(
    numeric_keypad_typing_sequences: TYPING_SEQUENCE,
    directional_keypad_typing_sequences: TYPING_SEQUENCE,
) -> int:
    return len(directional_keypad_typing_sequences) * int(
        numeric_keypad_typing_sequences.strip("A")
    )


def parse_input(data: str) -> set[TYPING_SEQUENCE]:
    data = data.strip("\n")
    return set(data.split("\n"))
