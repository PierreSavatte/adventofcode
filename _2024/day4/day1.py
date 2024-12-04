from _2024.day4 import compute_solution, parse_input
from _2024.load_input import load_input

if __name__ == "__main__":
    input_data = load_input(4)
    groups = parse_input(input_data)
    print(compute_solution(groups))
