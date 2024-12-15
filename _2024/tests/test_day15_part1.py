import pytest
from _2024.day15 import Direction, Warehouse, parse_input, to_gps
from _2024.day15.part1 import compute_solution

TEST_INPUT = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

TEST_INPUT_2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

WAREHOUSE = Warehouse(
    size=8,
    walls=[
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        (0, 1),
        (7, 1),
        (0, 2),
        (1, 2),
        (7, 2),
        (0, 3),
        (7, 3),
        (0, 4),
        (2, 4),
        (7, 4),
        (0, 5),
        (7, 5),
        (0, 6),
        (7, 6),
        (0, 7),
        (1, 7),
        (2, 7),
        (3, 7),
        (4, 7),
        (5, 7),
        (6, 7),
        (7, 7),
    ],
    boxes=[(3, 1), (5, 1), (4, 2), (4, 3), (4, 4), (4, 5)],
    robot=(2, 2),
    robot_moves=[
        Direction.LEFT,
        Direction.UP,
        Direction.UP,
        Direction.RIGHT,
        Direction.RIGHT,
        Direction.RIGHT,
        Direction.DOWN,
        Direction.DOWN,
        Direction.LEFT,
        Direction.DOWN,
        Direction.RIGHT,
        Direction.RIGHT,
        Direction.DOWN,
        Direction.LEFT,
        Direction.LEFT,
    ],
)


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == WAREHOUSE


def test_warehouse_can_be_displayed():
    assert (
        WAREHOUSE.to_str()
        == """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""
    )


@pytest.mark.parametrize(
    "direction, delta_position",
    [
        (Direction.UP, (0, -1)),
        (Direction.DOWN, (0, 1)),
        (Direction.RIGHT, (1, 0)),
        (Direction.LEFT, (-1, 0)),
    ],
)
def test_direction_can_give_delta_direction(direction, delta_position):
    assert direction.delta == delta_position


def test_warehouse_can_be_run_by_the_robot():
    steps = WAREHOUSE.run()

    expected_steps = [
        """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
        """
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
        """
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
        """
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
        """
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
        """
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########""",
        """
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########""",
        """
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########""",
        """
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########""",
        """
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########""",
        """
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########""",
        """
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########""",
        """
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########""",
        """
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########""",
        """
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########""",
    ]

    for step in expected_steps:
        next(steps)
        assert WAREHOUSE.to_str() == step


def test_more_complex_warehouse_can_be_run():
    warehouse = parse_input(TEST_INPUT_2)

    for _ in warehouse.run():
        ...

    assert (
        warehouse.to_str()
        == """
##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########"""
    )


def test_gps_coordinate_can_be_computed():
    position = (4, 1)
    assert to_gps(position) == 104


@pytest.mark.parametrize(
    "input, solution",
    [
        (TEST_INPUT, 2028),
        (TEST_INPUT_2, 10092),
    ],
)
def test_solution_can_be_computed(input, solution):
    warehouse = parse_input(input)
    assert compute_solution(warehouse) == solution
