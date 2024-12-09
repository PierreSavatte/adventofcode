from _2024.day9 import (
    Block,
    compact,
    compact_step,
    compute_checksum,
    flatten,
    get_first_available_free_space_index,
    get_last_available_file_index,
    parse_input,
)

TEST_INPUT = """2333133121414131402
"""
DISKMAP = [
    Block(0),
    Block(0),
    Block(None),
    Block(None),
    Block(None),
    Block(1),
    Block(1),
    Block(1),
    Block(None),
    Block(None),
    Block(None),
    Block(2),
    Block(None),
    Block(None),
    Block(None),
    Block(3),
    Block(3),
    Block(3),
    Block(None),
    Block(4),
    Block(4),
    Block(None),
    Block(5),
    Block(5),
    Block(5),
    Block(5),
    Block(None),
    Block(6),
    Block(6),
    Block(6),
    Block(6),
    Block(None),
    Block(7),
    Block(7),
    Block(7),
    Block(None),
    Block(8),
    Block(8),
    Block(8),
    Block(8),
    Block(9),
    Block(9),
]
FLAT_DISKMAP = "00...111...2...333.44.5555.6666.777.888899"


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == DISKMAP
    assert flatten(DISKMAP) == FLAT_DISKMAP


def test_disk_map_can_get_its_first_free_space():
    i = get_first_available_free_space_index(DISKMAP)

    assert i == 2


def test_disk_map_can_get_its_last_file():
    i = get_last_available_file_index(DISKMAP)

    assert i == 41


def test_disk_map_compaction_step_can_be_performed():
    disk_map = parse_input(TEST_INPUT)
    assert flatten(disk_map) == FLAT_DISKMAP

    for step in [
        "009..111...2...333.44.5555.6666.777.88889.",
        "0099.111...2...333.44.5555.6666.777.8888..",
        "00998111...2...333.44.5555.6666.777.888...",
        "009981118..2...333.44.5555.6666.777.88....",
        "0099811188.2...333.44.5555.6666.777.8.....",
        "009981118882...333.44.5555.6666.777.......",
        "0099811188827..333.44.5555.6666.77........",
        "00998111888277.333.44.5555.6666.7.........",
        "009981118882777333.44.5555.6666...........",
        "009981118882777333644.5555.666............",
        "00998111888277733364465555.66.............",
        "0099811188827773336446555566..............",
        "0099811188827773336446555566..............",
    ]:
        compact_step(disk_map)
        assert flatten(disk_map) == step


def test_disk_map_can_compact_itself():
    disk_map = parse_input(TEST_INPUT)
    assert (
        flatten(compact(disk_map))
        == "0099811188827773336446555566.............."
    )


def test_checksum_can_be_computed():
    new_disk_map = compact(DISKMAP)
    assert compute_checksum(new_disk_map) == 1928
