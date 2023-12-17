from _2023.day16 import Contraption, Direction, Position
from _2023.load_input import load_input
from tqdm import tqdm


def compute_solution(data: str) -> int:
    contraption = Contraption.from_data(data)
    max_energized_positions = 0

    def compute_max(position: Position, direction: Direction) -> int:
        energized_positions = contraption.compute_energized_positions(
            starting_position=position,
            starting_direction=direction,
        )
        nb_energized_positions = len(set(energized_positions))
        if nb_energized_positions > max_energized_positions:
            return nb_energized_positions
        else:
            return max_energized_positions

    print("First half of the computation...")
    for x in tqdm(range(contraption.max_x)):
        for y, direction in [
            (0, Direction.DOWN),
            (contraption.max_y, Direction.UP),
        ]:
            max_energized_positions = compute_max(
                position=(x, y), direction=direction
            )

    print("Second half of the computation...")
    for y in tqdm(range(contraption.max_y)):
        for x, direction in [
            (0, Direction.RIGHT),
            (contraption.max_x, Direction.LEFT),
        ]:
            max_energized_positions = compute_max(
                position=(x, y), direction=direction
            )

    return max_energized_positions


if __name__ == "__main__":
    print(compute_solution(load_input(16)))
