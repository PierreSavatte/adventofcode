from _2023.day3 import Schematic
from _2023.load_input import load_input


def compute_answer(data: str) -> int:
    schematic = Schematic.from_data(data)
    gears = schematic.get_gears()
    return sum(gear.ratio for gear in gears)


if __name__ == "__main__":
    print(compute_answer(load_input(3)))
