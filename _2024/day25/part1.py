from _2024.day25 import LocksAndKeys, parse_input
from _2024.load_input import load_input


def compute_solution(locks_and_keys: LocksAndKeys) -> int:
    return len(locks_and_keys.compute_fitting())


def main():
    input_data = load_input(25)
    locks_and_keys = parse_input(input_data)
    print(compute_solution(locks_and_keys))


if __name__ == "__main__":
    main()
