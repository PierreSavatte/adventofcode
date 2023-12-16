import pytest

from _2023.day16 import Lightbeam, Contraption, Tile, Direction, TileType
from _2023.day16.part1 import compute_solution


@pytest.mark.parametrize(
    "input_direction, new_position",
    [
        (Direction.UP, (3, 2)),
        (Direction.DOWN, (3, 4)),
        (Direction.RIGHT, (4, 3)),
        (Direction.LEFT, (2, 3)),
    ],
)
def test_lightbeam_encountering_empty_space_continues(
    input_direction, new_position
):
    lightbeam = Lightbeam(head=(3, 3), direction=input_direction)

    lightbeam.continues(Tile(type=TileType.EMPTY_SPACE, position=(3, 3)))

    assert lightbeam.head == new_position
    assert lightbeam.direction == input_direction


@pytest.mark.parametrize(
    "lightbeam, tile, expected_head, expected_direction",
    [
        (
            # >/
            Lightbeam(head=(3, 3), direction=Direction.RIGHT),
            Tile(type=TileType.MIRROR_UP, position=(3, 3)),
            (3, 2),
            Direction.UP,
        ),
        (
            # >\
            Lightbeam(head=(3, 3), direction=Direction.RIGHT),
            Tile(type=TileType.MIRROR_DOWN, position=(3, 3)),
            (3, 4),
            Direction.DOWN,
        ),
        (
            # /<
            Lightbeam(head=(3, 3), direction=Direction.LEFT),
            Tile(type=TileType.MIRROR_UP, position=(3, 3)),
            (3, 4),
            Direction.DOWN,
        ),
        (
            # \<
            Lightbeam(head=(3, 3), direction=Direction.LEFT),
            Tile(type=TileType.MIRROR_DOWN, position=(3, 3)),
            (3, 2),
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
            Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(3, 3)),
            (4, 3),
            Direction.RIGHT,
        ),
        (
            # -<
            Lightbeam(head=(3, 3), direction=Direction.LEFT),
            Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(3, 3)),
            (2, 3),
            Direction.LEFT,
        ),
        (
            # |
            # ^
            Lightbeam(head=(3, 3), direction=Direction.UP),
            Tile(type=TileType.SPLITTER_UP_DOWN, position=(3, 3)),
            (3, 2),
            Direction.UP,
        ),
        (
            # v
            # |
            Lightbeam(head=(3, 3), direction=Direction.DOWN),
            Tile(type=TileType.SPLITTER_UP_DOWN, position=(3, 3)),
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
            Tile(type=TileType.SPLITTER_UP_DOWN, position=(3, 3)),
            (3, 2),
            Direction.UP,
            (3, 4),
            Direction.DOWN,
        ),
        (
            # |<
            Lightbeam(head=(3, 3), direction=Direction.LEFT),
            Tile(type=TileType.SPLITTER_UP_DOWN, position=(3, 3)),
            (3, 2),
            Direction.UP,
            (3, 4),
            Direction.DOWN,
        ),
        (
            # -
            # ^
            Lightbeam(head=(3, 3), direction=Direction.UP),
            Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(3, 3)),
            (4, 3),
            Direction.RIGHT,
            (2, 3),
            Direction.LEFT,
        ),
        (
            # v
            # -
            Lightbeam(head=(3, 3), direction=Direction.DOWN),
            Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(3, 3)),
            (4, 3),
            Direction.RIGHT,
            (2, 3),
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
    assert lightbeam.direction == expected_direction
    assert new_lightbeam.head == expected_new_head
    assert new_lightbeam.direction == expected_new_direction


def test_lightbeam_stops_if_already_encountered_one_its_previous_state():
    # \..
    # -\.
    # \/.
    lightbeam = Lightbeam(head=(0, 0), direction=Direction.RIGHT)
    for accepted_tiles in [
        Tile(type=TileType.MIRROR_DOWN, position=(0, 0)),
        Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(0, 1)),
        Tile(type=TileType.MIRROR_DOWN, position=(1, 1)),
        Tile(type=TileType.MIRROR_UP, position=(1, 2)),
        Tile(type=TileType.MIRROR_DOWN, position=(0, 2)),
    ]:
        lightbeam.continues(accepted_tiles)

    with pytest.raises(StopIteration, match="already visited this tile"):
        lightbeam.continues(
            Tile(type=TileType.SPLITTER_RIGHT_LEFT, position=(0, 1))
        )


def test_contraption_can_be_parsed(get_data):
    contraption = Contraption.from_data(get_data("test_file_day16"))

    assert contraption.get_tile_at_position((0, 0)) == Tile(
        type=TileType.EMPTY_SPACE, position=(0, 0)
    )
    assert contraption.get_tile_at_position((1, 0)) == Tile(
        type=TileType.SPLITTER_UP_DOWN, position=(1, 0)
    )
    assert contraption.get_tile_at_position((9, 9)) == Tile(
        type=TileType.EMPTY_SPACE, position=(9, 9)
    )


def test_contraption_can_validate_position(get_data):
    contraption = Contraption.from_data(get_data("test_file_day16"))

    assert contraption.is_position_valid((0, 0)) is True
    assert contraption.is_position_valid((-1, 0)) is False
    assert contraption.is_position_valid((0, -1)) is False
    assert contraption.is_position_valid((3, 3)) is True
    assert contraption.is_position_valid((10, 0)) is False
    assert contraption.is_position_valid((0, 10)) is False


def test_solution_can_be_computed(get_data):
    data = get_data("test_file_day16")

    assert compute_solution(data) == 46
