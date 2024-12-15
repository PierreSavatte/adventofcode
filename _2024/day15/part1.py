from _2024.day15 import Warehouse, parse_input, to_gps
from _2024.load_input import load_input


def compute_solution(warehouse: Warehouse) -> int:
    for _ in warehouse.run():
        ...
    return sum([to_gps(box.gps_position) for box in warehouse.boxes])


def main():
    input_data = load_input(15)
    warehouse = parse_input(input_data)
    print(compute_solution(warehouse))


if __name__ == "__main__":
    main()
