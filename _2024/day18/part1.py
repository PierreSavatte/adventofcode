from _2024.day18 import Map, parse_input
from _2024.load_input import load_input


def compute_solution(map: Map) -> int:
    path = map.get_path()
    return len(path) - 1


def main():
    input_data = load_input(18)
    map = parse_input(input_data, map_size=70)
    map.current_fallen_bytes_number = 1024
    print(compute_solution(map))


if __name__ == "__main__":
    main()
