from typing import Generator


def parse_input(data: str) -> list[str]:
    return data.strip("\n").split("\n")


def get_windows(
    grid: list[str], window_size: int = 4
) -> Generator[list[str], None, None]:
    grid_size = len(grid)

    for y in range(0, grid_size - window_size + 1):
        for x in range(0, grid_size - window_size + 1):
            yield [
                grid[y_][x : x + window_size]
                for y_ in range(y, y + window_size)
            ]


def reverse_string(s: str) -> str:
    return "".join(reversed(s))


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
