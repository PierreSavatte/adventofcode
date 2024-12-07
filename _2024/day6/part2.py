from _2024.day6 import Map, parse_input
from _2024.load_input import load_input


def compute_solution(map: Map):
    return len(map.compute_new_obstacles_positions_to_form_loops())


def main():
    input_data = load_input(6)
    map = parse_input(input_data)
    print(compute_solution(map))


if __name__ == "__main__":
    main()
