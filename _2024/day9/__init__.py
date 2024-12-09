from typing import Optional

from tqdm import tqdm


class Block:
    def __init__(self, id: Optional[int]):
        self.id = id

    @property
    def displayable_id(self):
        return "." if self.id is None else str(self.id)

    def __eq__(self, other: "Block") -> bool:
        return self.id == other.id

    def __repr__(self) -> str:
        return f"<Block displayable_id={self.displayable_id}>"


DISK_MAP = list[Block]


def get_first_available_free_space_index(disk_map: DISK_MAP) -> int:
    for i, block in enumerate(disk_map):
        if block.id is None:
            return i


def get_last_available_file_index(disk_map: DISK_MAP) -> int:
    nb_blocks = len(disk_map)
    for i, block in enumerate(reversed(disk_map)):
        if block.id is not None:
            return nb_blocks - 1 - i


def compact_step(disk_map: DISK_MAP) -> DISK_MAP:
    file_index = get_last_available_file_index(disk_map)
    free_space_index = get_first_available_free_space_index(disk_map)

    if free_space_index < file_index:
        file_id = disk_map[file_index].id

        disk_map[file_index].id = None
        disk_map[free_space_index].id = file_id

    return disk_map


def compute_nb_free_space_to_replace(disk_map: DISK_MAP) -> int:
    return sum(block.id is None for block in disk_map)


def compact(disk_map: DISK_MAP) -> DISK_MAP:
    progress_bar = tqdm(total=compute_nb_free_space_to_replace(disk_map))
    old_map = flatten(disk_map)
    compact_step(disk_map)
    while flatten(disk_map) != old_map:
        old_map = flatten(disk_map)
        compact_step(disk_map)
        progress_bar.update(1)

    progress_bar.close()

    return disk_map


def compute_checksum(disk_map: DISK_MAP) -> int:
    checksum = 0
    for i, block in enumerate(disk_map):
        if block.id is not None:
            checksum += i * block.id

    return checksum


def flatten(disk_map: DISK_MAP) -> str:
    return "".join([block.displayable_id for block in disk_map])


def parse_input(data: str) -> DISK_MAP:
    data = data.strip("\n")

    blocks = []
    for i, char in enumerate(data):
        size = int(char)

        is_a_file = i % 2 == 0
        if is_a_file:
            id = i // 2
            block = id
        else:
            block = None

        blocks.extend([Block(block) for _ in range(size)])

    return blocks
