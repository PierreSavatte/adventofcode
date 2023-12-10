import pytest

from _2023.day10 import Tile, Map


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
        ("|", Tile.NORTH_SOUTH),
        ("-", Tile.EAST_WEST),
        ("L", Tile.NORTH_EAST),
        ("J", Tile.NORTH_WEST),
        ("7", Tile.SOUTH_WEST),
        ("F", Tile.SOUTH_EAST),
        (".", Tile.GROUND),
        ("S", Tile.STARTING_POSITION),
    ],
)
def test_tiles_can_be_computed(tile_character, expected_tile):
    assert Tile(tile_character) == expected_tile


def test_map_can_be_parsed_():
    map = Map.from_input(SIMPLE_MAP)

    assert map.tiles == [
        [Tile("."), Tile("."), Tile("."), Tile("."), Tile(".")],
        [Tile("."), Tile("S"), Tile("-"), Tile("7"), Tile(".")],
        [Tile("."), Tile("|"), Tile("."), Tile("|"), Tile(".")],
        [Tile("."), Tile("L"), Tile("-"), Tile("J"), Tile(".")],
        [Tile("."), Tile("."), Tile("."), Tile("."), Tile(".")],
    ]


@pytest.mark.parametrize(
    "input_data, expected_tiles",
    [
        (
            SQUARE_MAP,
            [
                [Tile("."), Tile("."), Tile("."), Tile("."), Tile(".")],
                [Tile("."), Tile("F"), Tile("-"), Tile("7"), Tile(".")],
                [Tile("."), Tile("|"), Tile("."), Tile("|"), Tile(".")],
                [Tile("."), Tile("L"), Tile("-"), Tile("J"), Tile(".")],
                [Tile("."), Tile("."), Tile("."), Tile("."), Tile(".")],
            ],
        ),
        (
            SIMPLE_MAP,
            [
                [Tile("."), Tile("."), Tile("."), Tile("."), Tile(".")],
                [Tile("."), Tile("S"), Tile("-"), Tile("7"), Tile(".")],
                [Tile("."), Tile("|"), Tile("."), Tile("|"), Tile(".")],
                [Tile("."), Tile("L"), Tile("-"), Tile("J"), Tile(".")],
                [Tile("."), Tile("."), Tile("."), Tile("."), Tile(".")],
            ],
        ),
        (
            REGULAR_MAP,
            [
                [Tile("-"), Tile("L"), Tile("|"), Tile("F"), Tile("7")],
                [Tile("7"), Tile("S"), Tile("-"), Tile("7"), Tile("|")],
                [Tile("L"), Tile("|"), Tile("7"), Tile("|"), Tile("|")],
                [Tile("-"), Tile("L"), Tile("-"), Tile("J"), Tile("|")],
                [Tile("L"), Tile("|"), Tile("-"), Tile("J"), Tile("F")],
            ],
        ),
        (
            MORE_COMPLEX_MAP,
            [
                [Tile("7"), Tile("-"), Tile("F"), Tile("7"), Tile("-")],
                [Tile("."), Tile("F"), Tile("J"), Tile("|"), Tile("7")],
                [Tile("S"), Tile("J"), Tile("L"), Tile("L"), Tile("7")],
                [Tile("|"), Tile("F"), Tile("-"), Tile("-"), Tile("J")],
                [Tile("L"), Tile("J"), Tile("."), Tile("L"), Tile("J")],
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
        Tile.EAST_WEST.get_connected_positions(tile_position=(1, 1))
        == expected_connected_positions
    )


@pytest.mark.parametrize(
    "tile_a, position_a, tile_b, position_b, expected_result",
    [
        # -7
        (Tile.EAST_WEST, (1, 1), Tile.SOUTH_WEST, (2, 1), True),
        # |
        # L
        (Tile.NORTH_SOUTH, (12, 4), Tile.NORTH_EAST, (12, 5), True),
        # 7-
        (Tile.EAST_WEST, (1, 1), Tile.SOUTH_WEST, (0, 1), False),
        # -.7
        (Tile.EAST_WEST, (1, 1), Tile.SOUTH_WEST, (3, 1), False),
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
