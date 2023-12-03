from _2023.day3 import Schematic

from _2023.load_input import load_input


def compute_answer(data: str) -> int:
    schematic = Schematic.from_data(data)

    part_numbers = []
    for number in schematic.numbers:
        if number.is_close_to_a_symbol(schematic.symbols):
            part_numbers.append(number)

    return sum(part_number.value for part_number in part_numbers)


if __name__ == "__main__":
    print(compute_answer(load_input(3)))
