from _2024.day15 import parse_input
from _2024.day15.part1 import compute_solution
from _2024.load_input import load_input


def main():
    input_data = load_input(15)
    warehouse = parse_input(input_data, large=True)
    print(compute_solution(warehouse))


if __name__ == "__main__":
    main()
