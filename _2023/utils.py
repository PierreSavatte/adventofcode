from copy import deepcopy
from typing import Any, Sequence

Table = Sequence[Sequence[Any]]


def transpose_table(table: Table) -> list[list[Any]]:
    table = deepcopy(table)

    table_col_length = len(table[0])
    table_row_length = len(table)

    new_table = [
        [0 for _ in range(table_row_length)] for _ in range(table_col_length)
    ]

    for x, line in enumerate(table):
        for y, item in enumerate(line):
            new_table[y][x] = item

    return new_table
