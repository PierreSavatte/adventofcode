from _2025.day7 import parse_diagram
from _2025.load_input import load_input


def main():
    diagram = parse_diagram(load_input(7))
    print(diagram.count_beams_that_has_split())


if __name__ == "__main__":
    main()
