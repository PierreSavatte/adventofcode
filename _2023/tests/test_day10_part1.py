import pytest

from _2023.day10 import Tile, TileType, Map

SQUARE_MAP = """.....
.F-7.
.|.|.
.L-J.
....."""

SIMPLE_MAP = """.....
.S-7.
.|.|.
.L-J.
....."""
EXPECTED_POSITION_SIMPLE_MAP = (1, 1)

REGULAR_MAP = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""
EXPECTED_POSITION_REGULAR_MAP = (1, 1)
EXPECTED_LOOP_POSITIONS_REGULAR_MAP = {
    (1, 1),
    (2, 1),
    (3, 1),
    (1, 2),
    (3, 2),
    (1, 3),
    (2, 3),
    (3, 3),
}
EXPECTED_DISTANCES_REGULAR_MAP = {
    (1, 1): 0,
    (2, 1): 1,
    (3, 1): 2,
    (1, 2): 1,
    (3, 2): 3,
    (1, 3): 2,
    (2, 3): 3,
    (3, 3): 4,
}

MORE_COMPLEX_MAP = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""
EXPECTED_POSITION_MORE_COMPLEX_MAP = (0, 2)
EXPECTED_LOOP_POSITIONS_MORE_COMPLEX_MAP = {
    (2, 0),
    (3, 0),
    (1, 1),
    (2, 1),
    (3, 1),
    (0, 2),
    (1, 2),
    (3, 2),
    (4, 2),
    (0, 3),
    (1, 3),
    (2, 3),
    (3, 3),
    (4, 3),
    (0, 4),
    (1, 4),
}
EXPECTED_DISTANCES_MORE_COMPLEX_MAP = {
    (2, 0): 4,
    (3, 0): 5,
    (1, 1): 2,
    (2, 1): 3,
    (3, 1): 6,
    (0, 2): 0,
    (1, 2): 1,
    (3, 2): 7,
    (4, 2): 8,
    (0, 3): 1,
    (1, 3): 4,
    (2, 3): 5,
    (3, 3): 6,
    (4, 3): 7,
    (0, 4): 2,
    (1, 4): 3,
}

MORE_COMPLEX_LOOP_MAP = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
EXPECTED_POSITION_MORE_COMPLEX_LOOP_MAP = (0, 2)


@pytest.mark.parametrize(
    "tile_character, expected_tile",
    [
        ("|", TileType.NORTH_SOUTH),
        ("-", TileType.EAST_WEST),
        ("L", TileType.NORTH_EAST),
        ("J", TileType.NORTH_WEST),
        ("7", TileType.SOUTH_WEST),
        ("F", TileType.SOUTH_EAST),
        (".", TileType.GROUND),
        ("S", TileType.STARTING_POSITION),
    ],
)
def test_tiles_can_be_computed(tile_character, expected_tile):
    assert TileType(tile_character) == expected_tile


@pytest.mark.parametrize(
    "input_data, expected_tiles",
    [
        (
            SQUARE_MAP,
            [
                [
                    Tile(position=(0, 0), type=TileType(".")),
                    Tile(position=(1, 0), type=TileType(".")),
                    Tile(position=(2, 0), type=TileType(".")),
                    Tile(position=(3, 0), type=TileType(".")),
                    Tile(position=(4, 0), type=TileType(".")),
                ],
                [
                    Tile(position=(0, 1), type=TileType(".")),
                    Tile(position=(1, 1), type=TileType("F")),
                    Tile(position=(2, 1), type=TileType("-")),
                    Tile(position=(3, 1), type=TileType("7")),
                    Tile(position=(4, 1), type=TileType(".")),
                ],
                [
                    Tile(position=(0, 2), type=TileType(".")),
                    Tile(position=(1, 2), type=TileType("|")),
                    Tile(position=(2, 2), type=TileType(".")),
                    Tile(position=(3, 2), type=TileType("|")),
                    Tile(position=(4, 2), type=TileType(".")),
                ],
                [
                    Tile(position=(0, 3), type=TileType(".")),
                    Tile(position=(1, 3), type=TileType("L")),
                    Tile(position=(2, 3), type=TileType("-")),
                    Tile(position=(3, 3), type=TileType("J")),
                    Tile(position=(4, 3), type=TileType(".")),
                ],
                [
                    Tile(position=(0, 4), type=TileType(".")),
                    Tile(position=(1, 4), type=TileType(".")),
                    Tile(position=(2, 4), type=TileType(".")),
                    Tile(position=(3, 4), type=TileType(".")),
                    Tile(position=(4, 4), type=TileType(".")),
                ],
            ],
        ),
        (
            SIMPLE_MAP,
            [
                [
                    Tile(position=(0, 0), type=TileType(".")),
                    Tile(position=(1, 0), type=TileType(".")),
                    Tile(position=(2, 0), type=TileType(".")),
                    Tile(position=(3, 0), type=TileType(".")),
                    Tile(position=(4, 0), type=TileType(".")),
                ],
                [
                    Tile(position=(0, 1), type=TileType(".")),
                    Tile(position=(1, 1), type=TileType("S")),
                    Tile(position=(2, 1), type=TileType("-")),
                    Tile(position=(3, 1), type=TileType("7")),
                    Tile(position=(4, 1), type=TileType(".")),
                ],
                [
                    Tile(position=(0, 2), type=TileType(".")),
                    Tile(position=(1, 2), type=TileType("|")),
                    Tile(position=(2, 2), type=TileType(".")),
                    Tile(position=(3, 2), type=TileType("|")),
                    Tile(position=(4, 2), type=TileType(".")),
                ],
                [
                    Tile(position=(0, 3), type=TileType(".")),
                    Tile(position=(1, 3), type=TileType("L")),
                    Tile(position=(2, 3), type=TileType("-")),
                    Tile(position=(3, 3), type=TileType("J")),
                    Tile(position=(4, 3), type=TileType(".")),
                ],
                [
                    Tile(position=(0, 4), type=TileType(".")),
                    Tile(position=(1, 4), type=TileType(".")),
                    Tile(position=(2, 4), type=TileType(".")),
                    Tile(position=(3, 4), type=TileType(".")),
                    Tile(position=(4, 4), type=TileType(".")),
                ],
            ],
        ),
        (
            REGULAR_MAP,
            [
                [
                    Tile(position=(0, 0), type=TileType("-")),
                    Tile(position=(1, 0), type=TileType("L")),
                    Tile(position=(2, 0), type=TileType("|")),
                    Tile(position=(3, 0), type=TileType("F")),
                    Tile(position=(4, 0), type=TileType("7")),
                ],
                [
                    Tile(position=(0, 1), type=TileType("7")),
                    Tile(position=(1, 1), type=TileType("S")),
                    Tile(position=(2, 1), type=TileType("-")),
                    Tile(position=(3, 1), type=TileType("7")),
                    Tile(position=(4, 1), type=TileType("|")),
                ],
                [
                    Tile(position=(0, 2), type=TileType("L")),
                    Tile(position=(1, 2), type=TileType("|")),
                    Tile(position=(2, 2), type=TileType("7")),
                    Tile(position=(3, 2), type=TileType("|")),
                    Tile(position=(4, 2), type=TileType("|")),
                ],
                [
                    Tile(position=(0, 3), type=TileType("-")),
                    Tile(position=(1, 3), type=TileType("L")),
                    Tile(position=(2, 3), type=TileType("-")),
                    Tile(position=(3, 3), type=TileType("J")),
                    Tile(position=(4, 3), type=TileType("|")),
                ],
                [
                    Tile(position=(0, 4), type=TileType("L")),
                    Tile(position=(1, 4), type=TileType("|")),
                    Tile(position=(2, 4), type=TileType("-")),
                    Tile(position=(3, 4), type=TileType("J")),
                    Tile(position=(4, 4), type=TileType("F")),
                ],
            ],
        ),
        (
            MORE_COMPLEX_MAP,
            [
                [
                    Tile(position=(0, 0), type=TileType("7")),
                    Tile(position=(1, 0), type=TileType("-")),
                    Tile(position=(2, 0), type=TileType("F")),
                    Tile(position=(3, 0), type=TileType("7")),
                    Tile(position=(4, 0), type=TileType("-")),
                ],
                [
                    Tile(position=(0, 1), type=TileType(".")),
                    Tile(position=(1, 1), type=TileType("F")),
                    Tile(position=(2, 1), type=TileType("J")),
                    Tile(position=(3, 1), type=TileType("|")),
                    Tile(position=(4, 1), type=TileType("7")),
                ],
                [
                    Tile(position=(0, 2), type=TileType("S")),
                    Tile(position=(1, 2), type=TileType("J")),
                    Tile(position=(2, 2), type=TileType("L")),
                    Tile(position=(3, 2), type=TileType("L")),
                    Tile(position=(4, 2), type=TileType("7")),
                ],
                [
                    Tile(position=(0, 3), type=TileType("|")),
                    Tile(position=(1, 3), type=TileType("F")),
                    Tile(position=(2, 3), type=TileType("-")),
                    Tile(position=(3, 3), type=TileType("-")),
                    Tile(position=(4, 3), type=TileType("J")),
                ],
                [
                    Tile(position=(0, 4), type=TileType("L")),
                    Tile(position=(1, 4), type=TileType("J")),
                    Tile(position=(2, 4), type=TileType(".")),
                    Tile(position=(3, 4), type=TileType("L")),
                    Tile(position=(4, 4), type=TileType("J")),
                ],
            ],
        ),
    ],
)
def test_map_can_be_parsed(input_data, expected_tiles):
    map = Map.from_input(input_data)

    assert map.tiles == expected_tiles


@pytest.mark.parametrize(
    "input_data", [SQUARE_MAP, SIMPLE_MAP, REGULAR_MAP, MORE_COMPLEX_MAP]
)
def test_map_can_be_output_as_str(input_data):
    map = Map.from_input(input_data)

    assert map.to_str() == input_data


@pytest.mark.parametrize(
    "input_data, expected_position",
    [
        (SIMPLE_MAP, EXPECTED_POSITION_SIMPLE_MAP),
        (REGULAR_MAP, EXPECTED_POSITION_REGULAR_MAP),
        (MORE_COMPLEX_MAP, EXPECTED_POSITION_MORE_COMPLEX_MAP),
        (MORE_COMPLEX_LOOP_MAP, EXPECTED_POSITION_MORE_COMPLEX_LOOP_MAP),
    ],
)
def test_starting_position_can_be_computed_from_map(
    input_data, expected_position
):
    map = Map.from_input(input_data)

    assert map.get_starting_position() == expected_position


def test_tile_can_give_its_tiles_its_connected_to():
    tile = Tile(type=TileType.EAST_WEST, position=(1, 1))
    expected_connected_positions = {
        (0, 1),
        (2, 1),
    }

    assert tile.get_connected_positions() == expected_connected_positions


@pytest.mark.parametrize(
    "tile_a, tile_b, expected_result",
    [
        # -7
        (
            Tile(type=TileType.EAST_WEST, position=(1, 1)),
            Tile(type=TileType.SOUTH_WEST, position=(2, 1)),
            True,
        ),
        # |
        # L
        (
            Tile(type=TileType.NORTH_SOUTH, position=(12, 4)),
            Tile(type=TileType.NORTH_EAST, position=(12, 5)),
            True,
        ),
        # 7-
        (
            Tile(type=TileType.EAST_WEST, position=(1, 1)),
            Tile(type=TileType.SOUTH_WEST, position=(0, 1)),
            False,
        ),
        # -.7
        (
            Tile(type=TileType.EAST_WEST, position=(1, 1)),
            Tile(type=TileType.SOUTH_WEST, position=(3, 1)),
            False,
        ),
    ],
)
def test_tiles_can_say_if_they_are_connected(tile_a, tile_b, expected_result):
    assert tile_a.is_connected_to(tile_b) is expected_result


@pytest.mark.parametrize(
    "input_data, expected_loop_positions",
    [
        (REGULAR_MAP, EXPECTED_LOOP_POSITIONS_REGULAR_MAP),
        (SIMPLE_MAP, EXPECTED_LOOP_POSITIONS_REGULAR_MAP),
        (MORE_COMPLEX_MAP, EXPECTED_LOOP_POSITIONS_MORE_COMPLEX_MAP),
        (MORE_COMPLEX_LOOP_MAP, EXPECTED_LOOP_POSITIONS_MORE_COMPLEX_MAP),
    ],
)
def test_map_can_compute_its_loop(input_data, expected_loop_positions):
    map = Map.from_input(input_data)

    loop = map.compute_loop()

    assert set(loop.positions) == expected_loop_positions


@pytest.mark.parametrize(
    "input_data, expected_distances",
    [
        (REGULAR_MAP, EXPECTED_DISTANCES_REGULAR_MAP),
        (SIMPLE_MAP, EXPECTED_DISTANCES_REGULAR_MAP),
        (MORE_COMPLEX_MAP, EXPECTED_DISTANCES_MORE_COMPLEX_MAP),
        (MORE_COMPLEX_LOOP_MAP, EXPECTED_DISTANCES_MORE_COMPLEX_MAP),
    ],
)
def test_map_can_compute_distances_in_loop(input_data, expected_distances):
    map = Map.from_input(input_data)

    loop = map.compute_loop()

    assert loop.distances == expected_distances
