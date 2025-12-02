import abc

from _2025.load_input import load_input


def parse_id_ranges(input: str) -> list[tuple[int, int]]:
    ids_tuple_list = input.strip().split(",")
    id_ranges = []
    for ids_tuple in ids_tuple_list:
        start, end = ids_tuple.split("-")
        id_ranges.append((int(start), int(end)))
    return id_ranges


class Solver:
    @abc.abstractmethod
    def is_invalid_id(id: int) -> bool:
        ...

    def get_invalid_ids(self, start: int, end: int) -> list[int]:
        return [id for id in range(start, end + 1) if self.is_invalid_id(id)]

    def compute_invalid_ids_sum(
        self, ids_tuple_list: list[tuple[int, int]]
    ) -> int:
        invalid_ids = []
        for ids_tuple in ids_tuple_list:
            invalid_ids.extend(self.get_invalid_ids(*ids_tuple))
        return sum(invalid_ids)

    def solve(self) -> int:
        ids_tuple_list = parse_id_ranges(load_input(2))
        return self.compute_invalid_ids_sum(ids_tuple_list)
