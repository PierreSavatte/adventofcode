from _2024.day9 import DISK_MAP, compact, compute_checksum, parse_input
from _2024.load_input import load_input


def compute_solution(disk_map: DISK_MAP) -> int:
    return compute_checksum(compact(disk_map))


def main():
    input_data = load_input(9)
    disk_map = parse_input(input_data)
    print(compute_solution(disk_map))


if __name__ == "__main__":
    main()
