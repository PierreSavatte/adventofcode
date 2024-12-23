from _2024.day23 import Computers, parse_input
from _2024.load_input import load_input


def compute_solution(computers: Computers) -> str:
    return ",".join(computers.get_largest_interconnected_set())


def main():
    input_data = load_input(23)
    computers = parse_input(input_data)
    print(compute_solution(computers))


if __name__ == "__main__":
    main()
