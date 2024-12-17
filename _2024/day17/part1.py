from _2024.day17 import Computer, parse_input
from _2024.load_input import load_input


def compute_solution(computer: Computer) -> str:
    result = computer.run()
    return ",".join(map(str, result))


def main():
    input_data = load_input(17)
    computer = parse_input(input_data)
    print(compute_solution(computer))


if __name__ == "__main__":
    main()
