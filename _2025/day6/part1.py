from _2025.day6 import BaseProblems, Problem
from _2025.load_input import load_input


class HumanProblems(BaseProblems):
    @staticmethod
    def parse_input(input: str) -> list[Problem]:
        lines = input.splitlines()
        nb_problems = len(lines[0].split())
        problems = [Problem() for _ in range(nb_problems)]
        for line in lines[:-1]:
            for i, value in enumerate(line.split()):
                problems[i].add_value(int(value))

        for i, operator in enumerate(lines[-1].split()):
            problems[i].set_operator(operator)

        return problems


def main():
    problems = HumanProblems(load_input(6))
    print(problems.compute_solution())


if __name__ == "__main__":
    main()
