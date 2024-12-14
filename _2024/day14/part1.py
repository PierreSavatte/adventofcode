from _2024.day14 import Simulation, parse_input
from _2024.load_input import load_input


def compute_solution(simulation: Simulation, time: int = 100) -> int:
    for t in range(time):
        for robot in simulation.robots:
            robot.move(simulation.map_size)

    robots_in_quadrants = simulation.count_robots_in_quadrants()

    solution = 1
    for value in robots_in_quadrants.values():
        solution *= value

    return solution


def main():
    input_data = load_input(14)
    simulation = parse_input(input_data, map_size=(101, 103))
    print(compute_solution(simulation))


if __name__ == "__main__":
    main()
