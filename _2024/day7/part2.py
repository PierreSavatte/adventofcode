from _2024.day7 import Operation, parse_input
from _2024.load_input import load_input


def mul(args):
    from operator import mul

    return mul(*args)


def concat(args):
    return int("".join(map(str, args)))


operators = [
    sum,
    mul,
    concat,
]


def compute_solution(operations: list[Operation]):
    return sum(
        operation.result
        for operation in operations
        if operation.can_be_made_true(operators)
    )


def main():
    input_data = load_input(7)
    operations = parse_input(input_data)
    print(compute_solution(operations))


if __name__ == "__main__":
    main()
