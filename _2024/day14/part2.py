from pathlib import Path

from _2024.day14 import Simulation, parse_input
from _2024.load_input import load_input
from PIL import Image

CURRENT_FOLDER = Path(__file__).parent.resolve()


def screenshot(simulation: Simulation, time: int):
    img = Image.new("1", simulation.map_size, 0)
    pixels = img.load()
    for x, y in simulation.robot_positions:
        pixels[x, y] = 1
    img.save(f"{time}.png")


def compute_solution(simulation: Simulation, end_time: int = 6494):
    for t in range(1, end_time):
        for robot in simulation.robots:
            robot.move(simulation.map_size)
        screenshot(simulation, t)


def main():
    input_data = load_input(14)
    simulation = parse_input(input_data, map_size=(101, 103))
    compute_solution(simulation)


if __name__ == "__main__":
    main()
