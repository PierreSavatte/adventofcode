from abc import ABC
from itertools import product
from typing import Any

from _2024.day10.a_star import PATH, Direction, a_star, euclidean_distance
from tqdm import tqdm

POSITION = tuple[int, int]
BUTTON = str
TYPING_SEQUENCE = str


def get_typing_sequence(path: list[POSITION]) -> list[str]:
    typing_sequence = []
    for a, b in zip(path, path[1:]):
        typing_sequence.append(Direction.from_two_points(a, b).to_str())
    return typing_sequence


def get_shortest(sequence: list) -> list:
    if len(sequence) < 2:
        return sequence
    min_length = min([len(item) for item in sequence])
    result = []
    for item in sequence:
        if len(item) == min_length:
            result.append(item)
    return result


def is_zigzag(typing_sequence: TYPING_SEQUENCE) -> bool:
    if len(typing_sequence) < 3:
        return False

    unique_characters = set(typing_sequence)
    if len(unique_characters) < 2:
        return False

    current = typing_sequence[0]
    already_seen_character = {current}
    for character in typing_sequence:
        if character != current:
            if character in already_seen_character:
                return True
            current = character
            already_seen_character.add(character)
    return False


class KeyPad(ABC):
    buttons: dict[BUTTON, POSITION]

    def __init__(self):
        self.cached_neighbors = {}
        self.cached_typing_sequences = {}

        self.build_shortest_typing_sequences()

    def build_shortest_typing_sequences(self):
        for start_button, start_position in self.buttons.items():
            for end_button, end_position in self.buttons.items():
                if start_button == end_button:
                    self.cached_typing_sequences[
                        (start_button, end_button)
                    ] = [""]
                    continue

                paths: list[PATH] = a_star(
                    map=None,
                    get_neighbors=self.get_neighbors,
                    start_position=start_position,
                    end_position=end_position,
                    distance_function=euclidean_distance,
                    multiple_optimal_paths=True,
                )

                built_paths = list(
                    map(lambda x: "".join(get_typing_sequence(x)), paths)
                )

                filtered_paths = []
                for path in built_paths:
                    if len(path) > 2:
                        if is_zigzag(path):
                            continue

                    filtered_paths.append(path)

                self.cached_typing_sequences[
                    (start_button, end_button)
                ] = get_shortest(filtered_paths)

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

    @property
    def start_position(self) -> POSITION:
        return self.buttons["A"]

    def _compute_shortest_typing_sequences(
        self, current_button: str, rest_of_the_buttons: str
    ) -> set[TYPING_SEQUENCE]:
        if rest_of_the_buttons == "":
            return set()

        next_button = rest_of_the_buttons[0]
        pre_sequences = self.cached_typing_sequences[
            current_button, next_button
        ]

        rest_of_the_buttons = rest_of_the_buttons[1:]
        post_sequences = self._compute_shortest_typing_sequences(
            next_button, rest_of_the_buttons
        )
        if len(post_sequences) == 0:
            return {f"{pre}A" for pre in pre_sequences}

        typing_sequences = {
            f"{pre}A{post}"
            for pre, post in product(pre_sequences, post_sequences)
        }
        return set(get_shortest(list(typing_sequences)))

    def compute_shortest_typing_sequences(
        self, typing_sequence: str
    ) -> set[TYPING_SEQUENCE]:
        return self._compute_shortest_typing_sequences(
            current_button="A", rest_of_the_buttons=typing_sequence
        )

    def compute_typing_sequences_from_typing_sequences(
        self, typing_sequences: set[TYPING_SEQUENCE]
    ) -> set[TYPING_SEQUENCE]:
        new_typing_sequences = set()
        progress_bar = tqdm(total=len(typing_sequences))
        for typing_sequence in typing_sequences:
            new_typing_sequences_for_current = (
                self.compute_shortest_typing_sequences(typing_sequence)
            )
            new_typing_sequences.update(new_typing_sequences_for_current)
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
