from _2025.day4 import Map
from _2025.load_input import load_input


def compute_solution(map: Map) -> int:
    accumulator = 0
    for cell in map.iterate_over_cells():
        nb_neighbours = cell.compute_nb_roll_neighbours()
        if nb_neighbours is not None and cell.compute_nb_roll_neighbours() < 4:
            accumulator += 1
    return accumulator


def main():
    map = Map(load_input(4))
    print(compute_solution(map))


if __name__ == "__main__":
    main()
