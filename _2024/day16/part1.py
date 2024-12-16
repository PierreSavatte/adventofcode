from _2024.day16 import Map, compute_total_distance, parse_input
from _2024.load_input import load_input


def compute_solution(map: Map) -> int:
    path = map.get_optimal_path()
    return compute_total_distance(path)


def main():
    input_data = load_input(16)
    map = parse_input(input_data)
    print(compute_solution(map))


if __name__ == "__main__":
    main()
