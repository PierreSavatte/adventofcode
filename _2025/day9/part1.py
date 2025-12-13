from _2025.day9 import compute_area, find_largest_rectangle, parse_input
from _2025.load_input import load_input


def main():
    points = parse_input(load_input(9))
    print(compute_area(*find_largest_rectangle(points)))


if __name__ == "__main__":
    main()
