from _2024.day6 import Map, compute_positions_in_a_line, parse_input
from _2024.load_input import load_input


def compute_solution(map: Map):
    positions = set()
    for line in map.get_traveling_lines():
        positions.update(compute_positions_in_a_line(*line))

    return len(positions)


def main():
    input_data = load_input(6)
    map = parse_input(input_data)
    print(compute_solution(map))


if __name__ == "__main__":
    main()
