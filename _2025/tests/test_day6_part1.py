import pytest
from _2025.day6 import Operator, Problem, Problems

TEST_INPUT = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_instructions_can_be_parsed():
    assert Problems(input=TEST_INPUT) == Problems(
        problems=[
            Problem(values=[123, 45, 6], operator=Operator.MULTIPLICATION),
            Problem(values=[328, 64, 98], operator=Operator.ADDITION),
            Problem(values=[51, 387, 215], operator=Operator.MULTIPLICATION),
            Problem(values=[64, 23, 314], operator=Operator.ADDITION),
        ]
    )


@pytest.mark.parametrize(
    "problem, expected_result",
    [
        (
            Problem(values=[123, 45, 6], operator=Operator.MULTIPLICATION),
            33210,
        ),
        (
            Problem(values=[328, 64, 98], operator=Operator.ADDITION),
            490,
        ),
        (
            Problem(values=[51, 387, 215], operator=Operator.MULTIPLICATION),
            4243455,
        ),
        (
            Problem(values=[64, 23, 314], operator=Operator.ADDITION),
            401,
        ),
    ],
)
def test_problems_can_be_solved(problem, expected_result):
    assert problem.solve() == expected_result


def test_solution_can_be_computed():
    assert Problems(input=TEST_INPUT).compute_solution() == 4277556
