import pytest

from _2023.day16 import Lightbeam, Contraption, Tile, Direction, TileType


@pytest.mark.parametrize(
    "input_direction",
    [Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT],
)
def test_lightbeam_encountering_empty_space_continues(input_direction):
    lightbeam = Lightbeam(head=(0, 0), direction=input_direction)

    lightbeam.continues(Tile(type=TileType.EMPTY_SPACE, position=(1, 0)))

    assert lightbeam.head == (1, 0)
    assert lightbeam.direction == input_direction


@pytest.mark.parametrize(
    "lightbeam, tile, expected_head, expected_direction",
    [
        (
            # >/
            Lightbeam(head=(3, 3), direction=Direction.RIGHT),
            Tile(type=TileType.MIRROR_UP, position=(4, 3)),
            (4, 3),
            Direction.UP,
        ),
        (
            # >\
            Lightbeam(head=(3, 3), direction=Direction.RIGHT),
            Tile(type=TileType.MIRROR_DOWN, position=(4, 3)),
            (4, 3),
            Direction.DOWN,
        ),
        (
            # /<
            Lightbeam(head=(3, 3), direction=Direction.LEFT),
            Tile(type=TileType.MIRROR_UP, position=(2, 3)),
            (2, 3),
            Direction.DOWN,
        ),
        (
            # \<
            Lightbeam(head=(3, 3), direction=Direction.LEFT),
            Tile(type=TileType.MIRROR_DOWN, position=(2, 3)),
            (2, 3),
            Direction.UP,
        ),
    ],
)
def test_lightbeam_encountering_mirror_is_reflected(
    lightbeam, tile, expected_head, expected_direction
):
    lightbeam.continues(tile)

    assert lightbeam.head == expected_head
    assert lightbeam.direction == expected_direction


@pytest.mark.parametrize(
    "lightbeam, tile, expected_head, expected_direction",
    [
        (
            # >-
            Lightbeam(head=(3, 3), direction=Direction.RIGHT),
            Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(4, 3)),
            (4, 3),
            Direction.RIGHT,
        ),
        (
            # -<
            Lightbeam(head=(3, 3), direction=Direction.LEFT),
            Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(2, 3)),
            (2, 3),
            Direction.LEFT,
        ),
        (
            # |
            # ^
            Lightbeam(head=(3, 3), direction=Direction.UP),
            Tile(type=TileType.SPLITTER_UP_DOWN, position=(3, 2)),
            (3, 2),
            Direction.UP,
        ),
        (
            # v
            # |
            Lightbeam(head=(3, 3), direction=Direction.DOWN),
            Tile(type=TileType.SPLITTER_UP_DOWN, position=(3, 4)),
            (3, 4),
            Direction.DOWN,
        ),
    ],
)
def test_lightbeam_encountering_pointy_end_of_splitter_continues(
    lightbeam, tile, expected_head, expected_direction
):
    lightbeam.continues(tile)

    assert lightbeam.head == expected_head
    assert lightbeam.direction == expected_direction


@pytest.mark.parametrize(
    "lightbeam, tile, expected_head, expected_direction, expected_new_head, expected_new_direction",
    [
        (
            # >|
            Lightbeam(head=(3, 3), direction=Direction.RIGHT),
            Tile(type=TileType.SPLITTER_UP_DOWN, position=(4, 3)),
            (4, 3),
            Direction.UP,
            (4, 3),
            Direction.DOWN,
        ),
        (
            # |<
            Lightbeam(head=(3, 3), direction=Direction.LEFT),
            Tile(type=TileType.SPLITTER_UP_DOWN, position=(2, 3)),
            (2, 3),
            Direction.UP,
            (2, 3),
            Direction.DOWN,
        ),
        (
            # -
            # ^
            Lightbeam(head=(3, 3), direction=Direction.UP),
            Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(3, 2)),
            (3, 2),
            Direction.RIGHT,
            (3, 2),
            Direction.LEFT,
        ),
        (
            # v
            # -
            Lightbeam(head=(3, 3), direction=Direction.DOWN),
            Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(3, 3)),
            (3, 3),
            Direction.RIGHT,
            (3, 3),
            Direction.LEFT,
        ),
    ],
)
def test_lightbeam_encountering_flat_side_of_splitter_splits(
    lightbeam,
    tile,
    expected_head,
    expected_direction,
    expected_new_head,
    expected_new_direction,
):
    new_lightbeam = lightbeam.continues(tile)

    assert lightbeam.head == expected_head
    assert new_lightbeam.head == expected_new_head


def test_lightbeam_stops_if_already_encountered_one_its_previous_state():
    ...


def test_lightbeam_path_can_be_computed():
    ...
