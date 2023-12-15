from dataclasses import dataclass
from typing import Optional

from _2023.day15 import compute_hash
from _2023.load_input import load_input


@dataclass
class Lens:
    label: str
    focal: Optional[int]


def get_index_lens_in_box(box: list[Lens], lens: Lens) -> Optional[int]:
    for i, lens_ in enumerate(box):
        if lens_.label == lens.label:
            return i
    return None


def is_lens_in_box(box: list[Lens], lens: Lens):
    return get_index_lens_in_box(box, lens) is not None


def remove_lens_from_box(box: list[Lens], lens: Lens):
    i = get_index_lens_in_box(box, lens)
    if i is not None:
        box.pop(i)


class Boxes(list):
    """
    Type of the object is list[list[Lens]]
    """

    def __init__(self):
        super().__init__(list([] for box_number in range(256)))

    def dash_operation(self, lens: Lens):
        box_number = compute_hash(lens.label)
        box = self[box_number]
        remove_lens_from_box(box, lens)

    def equals_operation(self, lens: Lens):
        box_number = compute_hash(lens.label)
        box = self[box_number]
        if is_lens_in_box(box, lens):
            i = get_index_lens_in_box(box, lens)
            box[i] = lens
        else:
            box.append(lens)

    def run_command(self, command: str):
        if "-" in command:
            label, _ = command.split("-")
            self.dash_operation(lens=Lens(label=label, focal=None))
        elif "=" in command:
            label, focal = command.split("=")
            self.equals_operation(lens=Lens(label=label, focal=int(focal)))
        else:
            RuntimeError(f"We got a problem {command}")


def compute_solution(data: str):
    boxes = Boxes()
    for command in data.split(","):
        boxes.run_command(command)

    focusing_power = 0
    for box_number, box in enumerate(boxes, start=1):
        for lens_number, lens in enumerate(box, start=1):
            focusing_power += box_number * lens_number * lens.focal

    return focusing_power


if __name__ == "__main__":
    print(compute_solution(load_input(15)))
