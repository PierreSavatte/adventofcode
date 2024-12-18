import random
from pathlib import Path

import matplotlib.pyplot as plt
from _2024.day12 import POSITION, Region, compute_regions, parse_input
from _2024.load_input import load_input
from tqdm import tqdm

COLOR = tuple[float, float, float]


def get_cell_color(regions: list[Region], position: POSITION) -> COLOR:
    for region in regions:
        if position in region.positions:
            return region.color


def generate_random_color() -> COLOR:
    return random.random(), random.random(), random.random()


def generate_image(map, regions, save=True, filename="input.png"):
    fig, ax = plt.subplots(figsize=(30, 30))
    map_size = len(map)

    # Draw the sides on the grid
    progress_bar = tqdm(total=len(regions))
    for region in regions:
        color = region.color = generate_random_color()

        for side in region.sides:
            x_range = side.x_range
            y_range = side.y_range

            if len(x_range) == 1:
                # Vertical line
                x = x_range[0]
                y_min, y_max = min(y_range), max(y_range)
                ax.plot(
                    [x, x],
                    [y_min, y_max],
                    "k-",
                    linewidth=5,
                    color=generate_random_color(),
                )
            elif len(y_range) == 1:
                # Horizontal line
                y = y_range[0]
                x_min, x_max = min(x_range), max(x_range)
                ax.plot(
                    [x_min, x_max],
                    [y, y],
                    "k-",
                    linewidth=5,
                    color=generate_random_color(),
                )

        progress_bar.update(1)
    progress_bar.close()

    # Add letters to the grid
    for y, row in enumerate(map):
        for x, letter in enumerate(row):
            rect = plt.Rectangle(
                (x, y),
                1,
                1,
                facecolor=get_cell_color(regions, (x, y)),
                alpha=0.3,
            )

            ax.add_patch(rect)
            ax.text(
                x + 0.5,
                y + 0.5,
                letter,
                ha="center",
                va="center",
                fontsize=5,
            )

    # Set the grid with the flipped y-axis
    ax.set_xticks(range(map_size + 1))
    ax.set_yticks(range(map_size + 1))
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)
    ax.set_xlim(-1, map_size + 1)
    ax.set_ylim(map_size + 1, -1)  # Flip the y-axis
    ax.set_aspect("equal")

    if save:
        plt.savefig(filename)
    else:
        plt.show()


if __name__ == "__main__":
    input_data = load_input(12)
    map = parse_input(input_data)
    regions = compute_regions(map)

    generate_image(map, regions)
