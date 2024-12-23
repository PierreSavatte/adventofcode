from _2024.day23 import Computers, one_computer_starts_with_t, parse_input
from _2024.load_input import load_input


def compute_solution(computers: Computers) -> int:
    return len(
        computers.compute_connected_sets(filter=one_computer_starts_with_t)
    )


def main():
    input_data = load_input(23)
    computers = parse_input(input_data)
    print(compute_solution(computers))


if __name__ == "__main__":
    main()
