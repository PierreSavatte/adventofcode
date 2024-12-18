from _2024.day18 import POSITION, Map, NoPathFound, parse_input
from _2024.load_input import load_input
from tqdm import tqdm


def compute_solution(map: Map) -> POSITION:
    previous_path = [map.obstacles[0]]
    progress_bar = tqdm(total=len(map.obstacles))
    for i in range(1, len(map.obstacles)):
        map.current_fallen_bytes_number = i

        new_byte = map.current_obstacles[-1]
        if new_byte not in previous_path:
            progress_bar.update()
            continue

        try:
            previous_path = map.get_path()
        except NoPathFound:
            progress_bar.close()
            return new_byte

        progress_bar.update()
    progress_bar.close()
    raise RuntimeError("Apparently no bytes are blocking the path 😅")


def main():
    input_data = load_input(18)
    map = parse_input(input_data, map_size=70)
    print(compute_solution(map))


if __name__ == "__main__":
    main()
