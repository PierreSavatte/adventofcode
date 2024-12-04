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
