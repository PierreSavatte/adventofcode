import pytest
from _2025.day6 import Operator, Problem
from _2025.day6.part2 import (
    CephalopodProblems,
    compute_reduced_matrice,
    extract_values_matrices,
    find_separators,
    transpose,
)

TEST_INPUT = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_separators_can_be_found():
    assert find_separators(TEST_INPUT) == [3, 7, 11]


def test_values_matrices_can_be_extracted():
    assert extract_values_matrices(
        input=TEST_INPUT, separators=[3, 7, 11]
    ) == [
        [
            ["1", "2", "3"],
            [" ", "4", "5"],
            [" ", " ", "6"],
        ],
        [
            ["3", "2", "8"],
            ["6", "4", " "],
            ["9", "8", " "],
        ],
        [
            [" ", "5", "1"],
            ["3", "8", "7"],
            ["2", "1", "5"],
        ],
        [
            ["6", "4", " "],
            ["2", "3", " "],
            ["3", "1", "4"],
        ],
    ]


@pytest.mark.parametrize(
    "matrice, expected_transposed_matrice",
    [
        (
            [
                ["1", "2", "3"],
                [" ", "4", "5"],
                [" ", " ", "6"],
            ],
            [
                ["1", " ", " "],
                ["2", "4", " "],
                ["3", "5", "6"],
            ],
        ),
        (
            [
                ["3", "2", "8"],
                ["6", "4", " "],
                ["9", "8", " "],
            ],
            [
                ["3", "6", "9"],
                ["2", "4", "8"],
                ["8", " ", " "],
            ],
        ),
        (
            [
                [" ", "5", "1"],
                ["3", "8", "7"],
                ["2", "1", "5"],
            ],
            [
                [" ", "3", "2"],
                ["5", "8", "1"],
                ["1", "7", "5"],
            ],
        ),
        (
            [
                ["6", "4", " "],
                ["2", "3", " "],
                ["3", "1", "4"],
            ],
            [
                ["6", "2", "3"],
                ["4", "3", "1"],
                [" ", " ", "4"],
            ],
        ),
        (
            [
                ["9", "5", "9", " "],
                ["1", "6", "2", "1"],
                ["3", "8", "1", "2"],
                ["4", "5", "9", "2"],
            ],
            [
                ["9", "1", "3", "4"],
                ["5", "6", "8", "5"],
                ["9", "2", "1", "9"],
                [" ", "1", "2", "2"],
            ],
        ),
        (
            [
                ["9", "5"],
                ["1", "6"],
                ["3", "8"],
                ["4", "5"],
            ],
            [
                ["9", "1", "3", "4"],
                ["5", "6", "8", "5"],
            ],
        ),
    ],
)
def test_matrice_can_be_transposed(matrice, expected_transposed_matrice):
    assert transpose(matrice) == expected_transposed_matrice


@pytest.mark.parametrize(
    "matrice, expected_reduced_matrice",
    [
        (
            [
                ["1", " ", " "],
                ["2", "4", " "],
                ["3", "5", "6"],
            ],
            [1, 24, 356],
        ),
        (
            [
                ["3", "6", "9"],
                ["2", "4", "8"],
                ["8", " ", " "],
            ],
            [369, 248, 8],
        ),
        (
            [
                [" ", "3", "2"],
                ["5", "8", "1"],
                ["1", "7", "5"],
            ],
            [32, 581, 175],
        ),
        (
            [
                ["6", "2", "3"],
                ["4", "3", "1"],
                [" ", " ", "4"],
            ],
            [623, 431, 4],
        ),
        (
            [
                ["9", "1", "3", "4"],
                ["5", "6", "8", "5"],
                ["9", "2", "1", "9"],
                [" ", "1", "2", "2"],
            ],
            [9134, 5685, 9219, 122],
        ),
        (
            [
                ["9", "1", "3", "4"],
                ["5", "6", "8", "5"],
            ],
            [9134, 5685],
        ),
    ],
)
def test_matrices_can_be_reduced(matrice, expected_reduced_matrice):
    assert compute_reduced_matrice(matrice) == expected_reduced_matrice


def test_instructions_can_be_parsed():
    assert CephalopodProblems(input=TEST_INPUT) == CephalopodProblems(
        problems=[
            Problem(values=[1, 24, 356], operator=Operator.MULTIPLICATION),
            Problem(values=[369, 248, 8], operator=Operator.ADDITION),
            Problem(values=[32, 581, 175], operator=Operator.MULTIPLICATION),
            Problem(values=[623, 431, 4], operator=Operator.ADDITION),
        ]
    )


def test_solution_can_be_computed():
    assert CephalopodProblems(input=TEST_INPUT).compute_solution() == 3263827
