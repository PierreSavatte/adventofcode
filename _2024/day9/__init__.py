from typing import Callable, Generator, Optional

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


class FileGroup:
    def __init__(self, id: int, start_index: int, size: int):
        self.id = id
        self.start_index = start_index
        self.size = size

    def __eq__(self, other: "FileGroup") -> bool:
        return (
            self.id == other.id
            and self.size == other.size
            and self.start_index == other.start_index
        )

    def __repr__(self) -> str:
        return (
            f"<FileGroup "
            f"id={self.id} "
            f"size={self.size} "
            f"start_index={self.start_index}>"
        )


class FreeSpace:
    def __init__(self, start_index: int, size: int):
        self.start_index = start_index
        self.size = size

    def __eq__(self, other: "FreeSpace") -> bool:
        return (
            self.size == other.size and self.start_index == other.start_index
        )

    def __repr__(self) -> str:
        return (
            f"<FreeSpace "
            f"size={self.size} "
            f"start_index={self.start_index}>"
        )


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


def get_file_groups(
    disk_map: DISK_MAP, min_size: Optional[int] = None
) -> Generator[FileGroup, FileGroup, None]:
    nb_blocks = len(disk_map)

    last_char = disk_map[-1].id
    file_size = 0
    i = nb_blocks - 1
    while i >= 0:
        char = disk_map[i].id
        if char != last_char:
            if last_char is not None:

                should_yield = True
                if min_size is not None:
                    should_yield = file_size >= min_size

                if should_yield:
                    yield FileGroup(
                        start_index=i + 1,
                        id=last_char,
                        size=file_size,
                    )

            file_size = 1
        else:
            file_size += 1

        last_char = char
        i -= 1


def get_free_spaces(
    disk_map: DISK_MAP, min_size: Optional[int] = None
) -> Generator[FileGroup, FileGroup, None]:
    previous_char = disk_map[0].id
    free_space_start = 0
    free_space_size = 0
    i = 1
    while i < len(disk_map):
        char = disk_map[i].id
        opening_free_space = char is None and previous_char is not None
        closing_free_space = previous_char is None and char is not None
        if closing_free_space:

            should_yield = True
            if min_size is not None:
                should_yield = free_space_size >= min_size

            if should_yield:
                yield FreeSpace(
                    start_index=free_space_start, size=free_space_size
                )

        if opening_free_space:
            free_space_start = i
            free_space_size = 0
        if char is None:
            free_space_size += 1

        previous_char = char
        i += 1


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


def smarter_compact_step(
    disk_map: DISK_MAP,
) -> Generator[DISK_MAP, DISK_MAP, None]:
    free_spaces = list(get_free_spaces(disk_map))
    for file_group in get_file_groups(disk_map):

        free_spaces_index = 0
        while free_spaces_index < len(free_spaces):
            free_space = free_spaces[free_spaces_index]
            if free_space.size >= file_group.size:
                free_spaces.pop(free_spaces_index)
                if free_space.size - file_group.size > 0:
                    free_spaces.insert(
                        free_spaces_index,
                        FreeSpace(
                            start_index=(
                                free_space.start_index + file_group.size
                            ),
                            size=free_space.size - file_group.size,
                        ),
                    )
            else:
                free_spaces_index += 1
                continue

            if free_space.start_index < file_group.start_index:

                for i in range(
                    file_group.start_index,
                    file_group.start_index + file_group.size,
                ):
                    disk_map[i].id = None
                for i in range(
                    free_space.start_index,
                    free_space.start_index + file_group.size,
                ):
                    disk_map[i].id = file_group.id

                yield disk_map
                break


def smarter_compact(disk_map: DISK_MAP) -> DISK_MAP:
    for _ in smarter_compact_step(disk_map):
        ...
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
