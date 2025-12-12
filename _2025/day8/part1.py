from _2025.day8 import Playground
from _2025.load_input import load_input


def main():
    playground = Playground.from_input(load_input(8))
    print(playground.compute_solution(nb_connections=1000))


if __name__ == "__main__":
    main()
