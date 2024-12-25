from dataclasses import dataclass

KEY = tuple[int, ...]
LOCK = tuple[int, ...]


@dataclass
class Lockset:
    key: KEY
    lock: LOCK


@dataclass
class LocksAndKeys:
    keys: list[KEY]
    locks: list[LOCK]

    def compute_fitting(self) -> list[Lockset]:
        locksets = []
        for lock in self.locks:
            for key in self.keys:
                fit = True
                for lock_pins, key_pins in zip(lock, key):
                    fit = fit and (lock_pins + key_pins <= 5)

                if fit:
                    locksets.append(Lockset(lock=lock, key=key))

        return locksets


def parse_input(data: str) -> LocksAndKeys:
    data = data.strip("\n")

    keys = []
    locks = []
    for item in data.split("\n\n"):
        lines = item.split("\n")
        first_line = lines.pop(0)
        last_line = lines.pop(-1)
        is_a_key = "." in first_line

        pin_height_per_column = {i: 0 for i in range(5)}
        for line in lines:
            for x, character in enumerate(line):
                if character == "#":
                    pin_height_per_column[x] += 1

        pin_heights = tuple(pin_height_per_column.values())
        if is_a_key:
            keys.append(pin_heights)
        else:
            locks.append(pin_heights)

    return LocksAndKeys(
        keys=keys,
        locks=locks,
    )
