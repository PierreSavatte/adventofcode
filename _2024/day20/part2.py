from _2024.day20 import Map, compute_shortcuts, parse_input
from _2024.load_input import load_input


def compute_solution(map: Map, min_save: int) -> int:
    path = map.compute_path()
    shortcuts = compute_shortcuts(
        path, min_time_saved=min_save, max_shortcut_size=20
    )
    return sum(shortcuts.values())


def main():
    input_data = load_input(20)
    map = parse_input(input_data)
    print(compute_solution(map, min_save=100))


if __name__ == "__main__":
    main()
