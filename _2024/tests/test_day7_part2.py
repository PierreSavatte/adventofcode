import pytest
from _2024.day7 import Operation
from _2024.day7.part2 import compute_solution, operators


@pytest.mark.parametrize(
    "operation, can_be_made_true",
    [
        (Operation(result=190, operands=[10, 19]), True),
        (Operation(result=3267, operands=[81, 40, 27]), True),
        (Operation(result=83, operands=[17, 5]), False),
        (Operation(result=156, operands=[15, 6]), True),
        (Operation(result=7290, operands=[6, 8, 6, 15]), True),
        (Operation(result=161011, operands=[16, 10, 13]), False),
        (Operation(result=192, operands=[17, 8, 14]), True),
        (Operation(result=21037, operands=[9, 7, 18, 13]), False),
        (Operation(result=292, operands=[11, 6, 16, 20]), True),
    ],
)
def test_operation_can_be_evaluated_if_can_be_made_true(
    operation, can_be_made_true
):
    assert operation.can_be_made_true(operators) == can_be_made_true


def test_solution_can_be_computed():
    assert (
        compute_solution(
            [
                Operation(result=190, operands=[10, 19]),
                Operation(result=3267, operands=[81, 40, 27]),
                Operation(result=83, operands=[17, 5]),
                Operation(result=156, operands=[15, 6]),
                Operation(result=7290, operands=[6, 8, 6, 15]),
                Operation(result=161011, operands=[16, 10, 13]),
                Operation(result=192, operands=[17, 8, 14]),
                Operation(result=21037, operands=[9, 7, 18, 13]),
                Operation(result=292, operands=[11, 6, 16, 20]),
            ]
        )
        == 11387
    )
