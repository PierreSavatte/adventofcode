import pytest

from _2023.day10 import TileType, Map

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

MORE_COMPLEX_MAP = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""
EXPECTED_POSITION_MORE_COMPLEX_MAP = (0, 2)

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


def test_map_can_be_parsed_():
    map = Map.from_input(SIMPLE_MAP)

    assert map.tiles == [
        [
            TileType("."),
            TileType("."),
            TileType("."),
            TileType("."),
            TileType("."),
        ],
        [
            TileType("."),
            TileType("S"),
            TileType("-"),
            TileType("7"),
            TileType("."),
        ],
        [
            TileType("."),
            TileType("|"),
            TileType("."),
            TileType("|"),
            TileType("."),
        ],
        [
            TileType("."),
            TileType("L"),
            TileType("-"),
            TileType("J"),
            TileType("."),
        ],
        [
            TileType("."),
            TileType("."),
            TileType("."),
            TileType("."),
            TileType("."),
        ],
    ]


@pytest.mark.parametrize(
    "input_data, expected_tiles",
    [
        (
            SQUARE_MAP,
            [
                [
                    TileType("."),
                    TileType("."),
                    TileType("."),
                    TileType("."),
                    TileType("."),
                ],
                [
                    TileType("."),
                    TileType("F"),
                    TileType("-"),
                    TileType("7"),
                    TileType("."),
                ],
                [
                    TileType("."),
                    TileType("|"),
                    TileType("."),
                    TileType("|"),
                    TileType("."),
                ],
                [
                    TileType("."),
                    TileType("L"),
                    TileType("-"),
                    TileType("J"),
                    TileType("."),
                ],
                [
                    TileType("."),
                    TileType("."),
                    TileType("."),
                    TileType("."),
                    TileType("."),
                ],
            ],
        ),
        (
            SIMPLE_MAP,
            [
                [
                    TileType("."),
                    TileType("."),
                    TileType("."),
                    TileType("."),
                    TileType("."),
                ],
                [
                    TileType("."),
                    TileType("S"),
                    TileType("-"),
                    TileType("7"),
                    TileType("."),
                ],
                [
                    TileType("."),
                    TileType("|"),
                    TileType("."),
                    TileType("|"),
                    TileType("."),
                ],
                [
                    TileType("."),
                    TileType("L"),
                    TileType("-"),
                    TileType("J"),
                    TileType("."),
                ],
                [
                    TileType("."),
                    TileType("."),
                    TileType("."),
                    TileType("."),
                    TileType("."),
                ],
            ],
        ),
        (
            REGULAR_MAP,
            [
                [
                    TileType("-"),
                    TileType("L"),
                    TileType("|"),
                    TileType("F"),
                    TileType("7"),
                ],
                [
                    TileType("7"),
                    TileType("S"),
                    TileType("-"),
                    TileType("7"),
                    TileType("|"),
                ],
                [
                    TileType("L"),
                    TileType("|"),
                    TileType("7"),
                    TileType("|"),
                    TileType("|"),
                ],
                [
                    TileType("-"),
                    TileType("L"),
                    TileType("-"),
                    TileType("J"),
                    TileType("|"),
                ],
                [
                    TileType("L"),
                    TileType("|"),
                    TileType("-"),
                    TileType("J"),
                    TileType("F"),
                ],
            ],
        ),
        (
            MORE_COMPLEX_MAP,
            [
                [
                    TileType("7"),
                    TileType("-"),
                    TileType("F"),
                    TileType("7"),
                    TileType("-"),
                ],
                [
                    TileType("."),
                    TileType("F"),
                    TileType("J"),
                    TileType("|"),
                    TileType("7"),
                ],
                [
                    TileType("S"),
                    TileType("J"),
                    TileType("L"),
                    TileType("L"),
                    TileType("7"),
                ],
                [
                    TileType("|"),
                    TileType("F"),
                    TileType("-"),
                    TileType("-"),
                    TileType("J"),
                ],
                [
                    TileType("L"),
                    TileType("J"),
                    TileType("."),
                    TileType("L"),
                    TileType("J"),
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
    expected_connected_positions = {
        (0, 1),
        (2, 1),
    }
    assert (
        TileType.EAST_WEST.get_connected_positions(tile_position=(1, 1))
        == expected_connected_positions
    )


@pytest.mark.parametrize(
    "tile_a, position_a, tile_b, position_b, expected_result",
    [
        # -7
        (TileType.EAST_WEST, (1, 1), TileType.SOUTH_WEST, (2, 1), True),
        # |
        # L
        (TileType.NORTH_SOUTH, (12, 4), TileType.NORTH_EAST, (12, 5), True),
        # 7-
        (TileType.EAST_WEST, (1, 1), TileType.SOUTH_WEST, (0, 1), False),
        # -.7
        (TileType.EAST_WEST, (1, 1), TileType.SOUTH_WEST, (3, 1), False),
    ],
)
def test_tiles_can_say_if_they_are_connected(
    tile_a, position_a, tile_b, position_b, expected_result
):
    assert (
        tile_a.is_connected_to(
            position=position_a, other=tile_b, other_position=position_b
        )
        is expected_result
    )
