from _2023.day14 import Platform
from _2023.day14.part1 import compute_solution

NO_ROUNDED_ROCKS_PLATFORM = """.....#....
....#....#
.....##...
...#......
........#.
..#....#.#
.....#....
..........
#....###..
#....#...."""

TILTED_PLATFORM = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""


def test_platform_can_be_parsed(get_data):
    data = get_data("test_file_day14")
    platform = Platform.from_input(data=data)

    assert platform.tiles == [
        ["O", ".", ".", ".", ".", "#", ".", ".", ".", "."],
        ["O", ".", "O", "O", "#", ".", ".", ".", ".", "#"],
        [".", ".", ".", ".", ".", "#", "#", ".", ".", "."],
        ["O", "O", ".", "#", "O", ".", ".", ".", ".", "O"],
        [".", "O", ".", ".", ".", ".", ".", "O", "#", "."],
        ["O", ".", "#", ".", ".", "O", ".", "#", ".", "#"],
        [".", ".", "O", ".", ".", "#", "O", ".", ".", "O"],
        [".", ".", ".", ".", ".", ".", ".", "O", ".", "."],
        ["#", ".", ".", ".", ".", "#", "#", "#", ".", "."],
        ["#", "O", "O", ".", ".", "#", ".", ".", ".", "."],
    ]

    assert platform.rounded_rocks_positions == [
        (0, 0),
        (0, 1),
        (2, 1),
        (3, 1),
        (0, 3),
        (1, 3),
        (4, 3),
        (9, 3),
        (1, 4),
        (7, 4),
        (0, 5),
        (5, 5),
        (2, 6),
        (6, 6),
        (9, 6),
        (7, 7),
        (1, 9),
        (2, 9),
    ]


def test_platform_can_get_tile_at_position(get_data):
    data = get_data("test_file_day14")
    platform = Platform.from_input(data=data)

    assert platform.get_tile_at_position((0, 0)) == "O"
    assert platform.get_tile_at_position((9, 0)) == "."
    assert platform.get_tile_at_position((9, 9)) == "."
    assert platform.get_tile_at_position((0, 9)) == "#"
    assert platform.get_tile_at_position((3, 5)) == "."


def test_platform_can_be_output_as_string(get_data):
    data = get_data("test_file_day14")
    platform = Platform.from_input(data=data)

    assert platform.as_str() == data


def test_tiles_with_no_rounded_rocks_can_be_computed(get_data):
    data = get_data("test_file_day14")
    platform = Platform.from_input(data=data)

    tiles = platform.compute_tiles_with_no_rounded_rocks()
    computed_platform = "\n".join(
        "".join(cell for cell in line) for line in tiles
    )

    assert computed_platform == NO_ROUNDED_ROCKS_PLATFORM


def test_platform_can_tilt_north(get_data):
    data = get_data("test_file_day14")
    platform = Platform.from_input(data=data)

    platform = platform.tilt_north()

    assert platform.as_str() == TILTED_PLATFORM


def test_load_can_be_computed_from_tilted_platform(get_data):
    data = get_data("test_file_day14")
    platform = Platform.from_input(data=data)

    platform = platform.tilt_north()

    assert platform.compute_load() == 136


def test_solution_can_be_computed(get_data):
    data = get_data("test_file_day14")
    assert compute_solution(data) == 136
