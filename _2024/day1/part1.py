from _2024.day1 import parse_input, get_distance_between_lists
from _2024.load_input import load_input


def main():
    input_data = load_input(1)
    lists = parse_input(input_data)
    print(get_distance_between_lists(*lists))


if __name__ == "__main__":
    main()
