from _2024.day12 import MAP, compute_regions, parse_input
from _2024.load_input import load_input


def compute_solution(map: MAP) -> int:
    regions = compute_regions(map)
    return sum(region.fence_price for region in regions)


def main():
    input_data = load_input(12)
    map = parse_input(input_data)
    print(compute_solution(map))


if __name__ == "__main__":
    main()
