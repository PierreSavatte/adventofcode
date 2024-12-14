import pytest
from _2024.day14 import Quadrant, Robot, Simulation, parse_input
from _2024.day14.part1 import compute_solution

TEST_INPUT = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

SIMULATION = Simulation(
    map_size=(11, 7),
    robots=[
        Robot(position=(0, 4), velocity=(3, -3)),
        Robot(position=(6, 3), velocity=(-1, -3)),
        Robot(position=(10, 3), velocity=(-1, 2)),
        Robot(position=(2, 0), velocity=(2, -1)),
        Robot(position=(0, 0), velocity=(1, 3)),
        Robot(position=(3, 0), velocity=(-2, -2)),
        Robot(position=(7, 6), velocity=(-1, -3)),
        Robot(position=(3, 0), velocity=(-1, -2)),
        Robot(position=(9, 3), velocity=(2, 3)),
        Robot(position=(7, 3), velocity=(-1, 2)),
        Robot(position=(2, 4), velocity=(2, -3)),
        Robot(position=(9, 5), velocity=(-3, -3)),
    ],
    simulation_time=100,
)


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT, map_size=(11, 7)) == SIMULATION


def test_robot_can_move():
    robot = Robot(position=(2, 4), velocity=(2, -3))

    robot.move(map_size=(11, 7))

    assert robot == Robot(position=(4, 1), velocity=(2, -3))


@pytest.mark.parametrize(
    "velocity, end_position",
    [
        ((-3, 0), (4, 2)),
        ((3, 0), (0, 2)),
        ((0, -3), (2, 4)),
        ((0, 3), (2, 0)),
    ],
)
def test_robot_teleports_on_the_other_side_of_the_map_if_needed(
    velocity, end_position
):
    robot = Robot(position=(2, 2), velocity=velocity)

    robot.move(map_size=(5, 5))

    assert robot == Robot(position=end_position, velocity=velocity)


def test_simulation_can_count_robots_in_quadrants():
    simulation = Simulation(
        map_size=(11, 7),
        robots=[
            Robot(position=(6, 0), velocity=(0, 0)),
            Robot(position=(6, 0), velocity=(0, 0)),
            Robot(position=(9, 0), velocity=(0, 0)),
            Robot(position=(0, 2), velocity=(0, 0)),
            Robot(position=(1, 3), velocity=(0, 0)),
            Robot(position=(2, 3), velocity=(0, 0)),
            Robot(position=(5, 4), velocity=(0, 0)),
            Robot(position=(3, 5), velocity=(0, 0)),
            Robot(position=(4, 5), velocity=(0, 0)),
            Robot(position=(4, 5), velocity=(0, 0)),
            Robot(position=(1, 6), velocity=(0, 0)),
            Robot(position=(6, 6), velocity=(0, 0)),
        ],
        simulation_time=100,
    )
    robots_in_quadrants = simulation.count_robots_in_quadrants()

    assert robots_in_quadrants == {
        Quadrant.I: 3,
        Quadrant.II: 1,
        Quadrant.III: 4,
        Quadrant.IV: 1,
    }


def test_solution_can_be_computed():
    assert compute_solution(SIMULATION) == 12
