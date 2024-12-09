import pytest
from _2024.day9 import (
    Block,
    FileGroup,
    FreeSpace,
    compact,
    compute_checksum,
    flatten,
    get_file_groups,
    get_free_spaces,
    parse_input,
    smarter_compact,
    smarter_compact_step,
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


def test_file_groups_can_be_computed():
    file_groups = get_file_groups(DISKMAP)

    assert next(file_groups) == FileGroup(id=9, start_index=40, size=2)
    assert next(file_groups) == FileGroup(id=8, start_index=36, size=4)
    assert next(file_groups) == FileGroup(id=7, start_index=32, size=3)


def test_file_groups_can_be_computed_with_a_filter():
    file_groups = get_file_groups(DISKMAP, min_size=3)

    assert next(file_groups) == FileGroup(id=8, start_index=36, size=4)
    assert next(file_groups) == FileGroup(id=7, start_index=32, size=3)


def test_disk_map_can_get_its_first_continuous_free_space():
    free_spaces = get_free_spaces(DISKMAP)

    assert next(free_spaces) == FreeSpace(start_index=2, size=3)
    assert next(free_spaces) == FreeSpace(start_index=8, size=3)
    assert next(free_spaces) == FreeSpace(start_index=12, size=3)
    assert next(free_spaces) == FreeSpace(start_index=18, size=1)
    assert next(free_spaces) == FreeSpace(start_index=21, size=1)


def test_disk_map_can_get_its_first_continuous_free_space_with_a_filter():
    free_spaces = get_free_spaces(DISKMAP, min_size=2)

    assert next(free_spaces) == FreeSpace(start_index=2, size=3)
    assert next(free_spaces) == FreeSpace(start_index=8, size=3)
    assert next(free_spaces) == FreeSpace(start_index=12, size=3)
    with pytest.raises(StopIteration):
        next(free_spaces)


def test_disk_map_smarter_compaction_step_can_be_performed():
    disk_map = parse_input(TEST_INPUT)
    assert flatten(disk_map) == FLAT_DISKMAP

    smarter_compact_step_generator = smarter_compact_step(disk_map)
    for step in [
        "0099.111...2...333.44.5555.6666.777.8888..",
        "0099.1117772...333.44.5555.6666.....8888..",
        "0099.111777244.333....5555.6666.....8888..",
        "00992111777.44.333....5555.6666.....8888..",
    ]:
        next(smarter_compact_step_generator)
        assert flatten(disk_map) == step


def test_disk_map_can_compact_itself():
    disk_map = parse_input(TEST_INPUT)
    assert (
        flatten(smarter_compact(disk_map))
        == "00992111777.44.333....5555.6666.....8888.."
    )


def test_checksum_can_be_computed():
    new_disk_map = smarter_compact(DISKMAP)
    assert compute_checksum(new_disk_map) == 2858
