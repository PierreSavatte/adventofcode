from collections.abc import Callable
from enum import Enum
from functools import reduce
from typing import Optional

from _2025.load_input import load_input


class Operator(Enum):
    ADDITION = "+"
    MULTIPLICATION = "*"

    def get_implementation(self) -> Callable[[int, int], int]:
        if self == Operator.ADDITION:
            return lambda a, b: a + b
        if self == Operator.MULTIPLICATION:
            return lambda a, b: a * b

        raise RuntimeError(f"Operator {self} is not supported")


class Problem:
    def __init__(
        self,
        values: Optional[list[int]] = None,
        operator: Optional[Operator] = None,
    ):
        self.values = values or []
        self.operator = operator

    def add_value(self, value: int):
        self.values.append(value)

    def set_operator(self, operator: str):
        self.operator = Operator(operator)

    def solve(self) -> int:
        function = self.operator.get_implementation()
        return reduce(function, self.values)

    def __str__(self) -> str:
        operator = None if not self.operator else self.operator.value
        return f"Problem<values={[value for value in self.values]}; operator={operator}>"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Problem):
            return False
        return self.values == other.values and self.operator == other.operator


class Problems:
    def __init__(
        self,
        input: Optional[str] = None,
        problems: Optional[list[Problem]] = None,
    ):
        if input is None and problems is None:
            raise RuntimeError("One value must be provided.")
        if problems:
            self.problems = problems
        if input:
            lines = input.splitlines()
            nb_problems = len(lines[0].split())
            self.problems = [Problem() for _ in range(nb_problems)]
            for line in lines[:-1]:
                for i, value in enumerate(line.split()):
                    self.problems[i].add_value(int(value))

            for i, operator in enumerate(lines[-1].split()):
                self.problems[i].set_operator(operator)

    def compute_solution(self) -> int:
        return sum(problem.solve() for problem in self.problems)

    def __str__(self) -> str:
        return str([problem for problem in self.problems])

    def __repr__(self):
        return str(self)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Problems):
            return False
        return self.problems == other.problems


def main():
    problems = Problems(load_input(6))
    print(problems.compute_solution())


if __name__ == "__main__":
    main()
