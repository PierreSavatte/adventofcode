from _2024.day16 import Map, parse_input
from _2024.load_input import load_input


def compute_solution(map: Map) -> int:
    all_paths_cells = set()
    all_paths = map.get_all_optimal_paths()
    for path in all_paths:
        all_paths_cells.update(path)

    return len(all_paths_cells)


def main():
    input_data = load_input(16)
    map = parse_input(input_data)
    print(compute_solution(map))


if __name__ == "__main__":
    main()
