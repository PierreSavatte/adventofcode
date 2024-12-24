from _2024.day24 import Computer, parse_input
from _2024.load_input import load_input


def compute_solution(computer: Computer) -> int:
    computer.run()
    return computer.read_output()


def main():
    input_data = load_input(24)
    computers = parse_input(input_data)
    print(compute_solution(computers))


if __name__ == "__main__":
    main()
