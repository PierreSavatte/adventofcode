from _2024.day24 import Computer, parse_input
from _2024.load_input import load_input


def compute_solution(computer: Computer) -> str:
    cables_to_swipe = sorted(computer.get_cables_to_swipe())
    return ",".join(cables_to_swipe)


def main():
    input_data = load_input(24)
    computers = parse_input(input_data)
    print(compute_solution(computers))


if __name__ == "__main__":
    main()
