from _2024.day4 import get_windows, parse_input, reverse_string
from _2024.load_input import load_input


def is_x_mas(window: list[str]) -> bool:
    window_size = len(window)

    first_diagonal = "".join(window[x][x] for x in range(window_size))
    second_diagonal = "".join(
        window[window_size - 1 - x][x] for x in range(window_size)
    )

    options = [
        (first_diagonal, second_diagonal),
        (reverse_string(first_diagonal), reverse_string(second_diagonal)),
        (first_diagonal, reverse_string(second_diagonal)),
        (reverse_string(first_diagonal), second_diagonal),
    ]

    return any(all(word == "MAS" for word in option) for option in options)


def compute_solution(grid: list[str]) -> int:
    solution = 0

    for window in get_windows(grid, window_size=3):
        if is_x_mas(window):
            solution += 1

    return solution


if __name__ == "__main__":
    input_data = load_input(4)
    groups = parse_input(input_data)
    print(compute_solution(groups))
