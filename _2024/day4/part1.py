from _2024.day4 import get_windows, parse_input, reverse_string
from _2024.load_input import load_input


def compute_xmax_number_in_diagonals(window: list[str]) -> int:
    count = 0

    window_size = len(window)
    first_diagonal = "".join(window[x][x] for x in range(window_size))
    second_diagonal = "".join(
        window[window_size - 1 - x][x] for x in range(window_size)
    )
    options = [
        # first diagonal
        first_diagonal,
        # first reverse diagonal
        reverse_string(first_diagonal),
        # second diagonal
        second_diagonal,
        # second reverse diagonal
        reverse_string(second_diagonal),
    ]

    for option in options:
        if option == "XMAS":
            count += 1

    return count


def compute_xmax_number_in_rows(grid: list[str]) -> int:
    grid_size = len(grid)
    window_size = 4
    count = 0
    for row in grid:
        for x in range(grid_size - window_size + 1):
            word = row[x : x + window_size]
            options = [word, reverse_string(word)]
            for option in options:
                if option == "XMAS":
                    count += 1

    return count


def transpose(grid: list[str]) -> list[str]:
    grid_size = len(grid)

    new_grid = []

    for x in range(grid_size):
        line = "".join([grid[y][x] for y in range(grid_size)])
        new_grid.append(line)

    return new_grid


def compute_solution(grid: list[str]) -> int:
    solution = 0

    # Count rows
    solution += compute_xmax_number_in_rows(grid)

    # Count columns
    transposed_grid = transpose(grid)
    solution += compute_xmax_number_in_rows(transposed_grid)

    # Count diagonals
    for window in get_windows(grid):
        xmax_number = compute_xmax_number_in_diagonals(window)
        solution += xmax_number

    return solution


if __name__ == "__main__":
    input_data = load_input(4)
    groups = parse_input(input_data)
    print(compute_solution(groups))
