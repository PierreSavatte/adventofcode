import re
from collections import defaultdict
from functools import reduce

from _2025.day6 import BaseProblems, Problem
from _2025.load_input import load_input

MATRICE = list[list[str]]


def intersection(a: set, b: set) -> set:
    return a.intersection(b)


def find_separators(input: str) -> list[int]:
    lines = input.splitlines()

    all_cols_with_spaces = []
    for line in lines[:-1]:
        cols_with_spaces = {match.start() for match in re.finditer(" ", line)}
        all_cols_with_spaces.append(cols_with_spaces)

    separators = reduce(intersection, all_cols_with_spaces)
    return sorted(list(separators))


def extract_values_matrices(
    input: str, separators: list[int]
) -> list[MATRICE]:
    matrices = defaultdict(lambda: defaultdict(list))
    input_values = input.strip().splitlines()[:-1]

    line_length = len(input_values[0])
    separators = [0, *separators, line_length]
    for line_index, line in enumerate(input_values):
        for matrice_index, (i, j) in enumerate(
            zip(separators, separators[1:])
        ):
            if i > 0:
                # To skip the index i that is the separator index on
                # other values than the first
                i += 1
            matrices[matrice_index][line_index].extend(list(line[i:j]))
    return [
        [item for item in matrice.values()] for matrice in matrices.values()
    ]


def transpose(matrice: MATRICE) -> MATRICE:
    target_height = len(matrice[0])
    target_width = len(matrice)

    target = []
    for y in range(target_height):
        target.append([matrice[x][y] for x in range(target_width)])

    return target


def compute_reduced_matrice(matrice: MATRICE) -> list[int]:
    return [int("".join(line).strip()) for line in matrice]


class CephalopodProblems(BaseProblems):
    @staticmethod
    def parse_input(input: str) -> list[Problem]:
        lines = input.splitlines()

        separators = find_separators(input)

        values_list = map(
            compute_reduced_matrice,
            map(
                transpose,
                extract_values_matrices(input, separators),
            ),
        )

        problems = [Problem(values) for values in values_list]
        for i, operator in enumerate(lines[-1].split()):
            problems[i].set_operator(operator)

        return problems


def main():
    problems = CephalopodProblems(load_input(6))
    print(problems.compute_solution())


if __name__ == "__main__":
    main()
