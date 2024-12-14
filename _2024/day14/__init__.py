from dataclasses import dataclass
from enum import Enum

MAP_SIZE = tuple[int, int]
POSITION = tuple[int, int]
VELOCITY = tuple[int, int]


class Quadrant(Enum):
    I = "I"
    II = "II"
    III = "III"
    IV = "IV"


@dataclass
class Robot:
    position: POSITION
    velocity: VELOCITY

    def move(self, map_size: MAP_SIZE):
        x, y = self.position
        delta_x, delta_y = self.velocity

        new_x = x + delta_x
        new_y = y + delta_y

        map_width, map_height = map_size
        if new_x < 0:
            new_x += map_width
        if new_y < 0:
            new_y += map_height
        if new_x >= map_width:
            new_x -= map_width
        if new_y >= map_height:
            new_y -= map_height

        self.position = new_x, new_y


@dataclass
class Simulation:
    map_size: MAP_SIZE
    robots: list[Robot]
    simulation_time: int = 100

    @property
    def robot_positions(self) -> list[POSITION]:
        return [robot.position for robot in self.robots]

    def count_robots_in_quadrants(self) -> dict[Quadrant, int]:
        robots_in_quadrants = {
            Quadrant.I: 0,
            Quadrant.II: 0,
            Quadrant.III: 0,
            Quadrant.IV: 0,
        }

        width, height = self.map_size
        half_width = width // 2
        half_height = height // 2

        for x, y in self.robot_positions:
            quadrant = None
            if 0 <= x < half_width:
                if 0 <= y < half_height:
                    quadrant = Quadrant.II
                elif half_height < y < height:
                    quadrant = Quadrant.III
            elif half_width < x < width:
                if 0 <= y < half_height:
                    quadrant = Quadrant.I
                elif half_height < y < height:
                    quadrant = Quadrant.IV

            if quadrant:
                robots_in_quadrants[quadrant] += 1

        return robots_in_quadrants


def parse_int_tuple(data: str) -> tuple[int, int]:
    data = data.split("=")[-1]
    x_data, y_data = data.split(",")
    return int(x_data), int(y_data)


def parse_input(data: str, map_size: MAP_SIZE) -> Simulation:
    data = data.strip("\n")

    robots = []
    for line in data.split("\n"):
        position_data, velocity_data = line.split(" ")

        position = parse_int_tuple(position_data)
        velocity = parse_int_tuple(velocity_data)
        robots.append(
            Robot(
                position=position,
                velocity=velocity,
            )
        )

    return Simulation(map_size=map_size, robots=robots)
