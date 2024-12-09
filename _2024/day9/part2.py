from _2024.day9 import DISK_MAP, compute_checksum, parse_input, smarter_compact
from _2024.load_input import load_input


def compute_solution(disk_map: DISK_MAP) -> int:
    return compute_checksum(smarter_compact(disk_map))


def main():
    input_data = load_input(9)
    disk_map = parse_input(input_data)
    print(compute_solution(disk_map))


if __name__ == "__main__":
    main()
