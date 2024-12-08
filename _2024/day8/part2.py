from _2024.day8 import Map, parse_input
from _2024.load_input import load_input


def compute_solution(map: Map) -> int:
    antinodes = map.compute_antinodes_with_resonance()
    antinodes_points = set()
    for k, antinodes_list in antinodes.items():
        antinodes_points.update(antinodes_list)
    return len(antinodes_points)


def main():
    input_data = load_input(8)
    map = parse_input(input_data)
    print(compute_solution(map))


if __name__ == "__main__":
    main()
