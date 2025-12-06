from _2025.day4 import Map
from _2025.load_input import load_input


def compute_solution(map: Map) -> int:
    accumulator = 0
    has_removed_roll = True
    while has_removed_roll:
        current_positions_to_remove = []
        for cell in map.iterate_over_cells():
            nb_neighbours = cell.compute_nb_roll_neighbours()
            if (
                nb_neighbours is not None
                and cell.compute_nb_roll_neighbours() < 4
            ):
                current_positions_to_remove.append(cell.position)

        has_removed_roll = len(current_positions_to_remove) > 0
        accumulator += len(current_positions_to_remove)
        for position in current_positions_to_remove:
            map.get_cell(position).is_roll = False
    return accumulator


def main():
    map = Map(load_input(4))
    print(compute_solution(map))


if __name__ == "__main__":
    main()
