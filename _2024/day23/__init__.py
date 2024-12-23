import math
from functools import cache
from itertools import combinations
from typing import Callable, Optional

from tqdm import tqdm

COMPUTER = str


def one_computer_starts_with_t(computers: tuple[COMPUTER, ...]) -> bool:
    return any(computer.startswith("t") for computer in computers)


class Computers:
    def __init__(self, connected_computers: list[tuple[COMPUTER, COMPUTER]]):
        self.connected_computers = connected_computers

        self.computers = set()

        for connected_computers in self.connected_computers:
            self.computers.update([*connected_computers])

    @cache
    def are_connected(
        self, computer_a: COMPUTER, computer_b: COMPUTER
    ) -> bool:
        one_way = (computer_a, computer_b) in self.connected_computers
        another = (
            computer_b,
            computer_a,
        ) in self.connected_computers

        return one_way or another

    def compute_connected_sets(
        self, n: int = 3, filter: Optional[Callable] = None
    ) -> set[tuple[COMPUTER, ...]]:
        connected_sets = set()
        combinations_length = math.comb(len(self.computers), n)
        progress_bar = tqdm(total=combinations_length)
        for computers in combinations(self.computers, n):
            are_all_interconnected = all(
                self.are_connected(computer_a, computer_b)
                for computer_a, computer_b in combinations(computers, 2)
            )
            if are_all_interconnected:
                pass_filter = True
                if filter:
                    pass_filter = filter(computers)

                if pass_filter:
                    connected_sets.add(tuple(sorted(computers)))
            progress_bar.update()
        progress_bar.close()
        return connected_sets


def parse_input(data: str) -> Computers:
    data = data.strip("\n")

    connected_computers = []
    for computers in data.split("\n"):
        computer_a, computer_b = computers.split("-")
        connected_computers.append((computer_a, computer_b))

    return Computers(connected_computers=connected_computers)
