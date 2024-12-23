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

    def get_neighbors(self, computer: COMPUTER) -> list[COMPUTER]:
        neighbors = set()
        for connected_computers in self.connected_computers:
            if computer in connected_computers:
                neighbors.update([*connected_computers])

        neighbors.remove(computer)
        return list(sorted(neighbors))

    @cache
    def are_connected(
        self, computer_a: COMPUTER, computer_b: COMPUTER
    ) -> bool:
        one_way = (computer_a, computer_b) in self.connected_computers
        another = (computer_b, computer_a) in self.connected_computers
        return one_way or another

    def compute_connected_sets(
        self, n: int = 3, filter: Optional[Callable] = None
    ) -> set[tuple[COMPUTER, ...]]:
        connected_sets = set()
        combinations_length = math.comb(len(self.computers), n)
        progress_bar = tqdm(total=combinations_length)
        for computers in combinations(self.computers, n):
            computers = tuple(sorted(computers))
            are_all_interconnected = all(
                self.are_connected(computer_a, computer_b)
                for computer_a, computer_b in combinations(computers, 2)
            )
            if are_all_interconnected:
                pass_filter = True
                if filter is not None:
                    pass_filter = filter(computers)

                if pass_filter:
                    connected_sets.add(computers)
            progress_bar.update()
        progress_bar.close()
        return connected_sets

    def bron_kerbosch(
        self,
        r: set[COMPUTER, ...],
        p: set[COMPUTER, ...],
        x: set[COMPUTER, ...],
    ):
        # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm#Without_pivoting
        if len(p) == 0 and len(x) == 0:
            return [r]
        temp_p = p.copy()
        cliques = []
        for v in p:
            new_R = r.union({v})
            v_neighbors = self.get_neighbors(v)
            new_P = temp_p.intersection(v_neighbors)
            new_X = x.intersection(v_neighbors)
            cliques.extend(self.bron_kerbosch(new_R, new_P, new_X))
            temp_p.remove(v)
            x.add(v)
        return cliques

    def get_largest_interconnected_set(self):
        r = set()
        p = set(self.computers)
        x = set()
        cliques = self.bron_kerbosch(r, p, x)

        max_clique = None
        max_length = 0
        for clique in cliques:
            clique_length = len(clique)
            if clique_length >= max_length:
                max_length = clique_length
                max_clique = clique

        return tuple(sorted(max_clique))


def parse_input(data: str) -> Computers:
    data = data.strip("\n")

    connected_computers = []
    for computers in data.split("\n"):
        computer_a, computer_b = computers.split("-")
        connected_computers.append((computer_a, computer_b))

    return Computers(connected_computers=connected_computers)
