def mul(args):
    from operator import mul

    return mul(*args)


operators = [
    sum,
    mul,
]


class Operation:
    def __init__(self, result: int, operands: list[int]):
        self.result = result
        self.operands = operands

    def __repr__(self) -> str:
        return f"<Operation result={self.result} operands={self.operands}>"

    def __eq__(self, other: "Operation") -> bool:
        return self.result == other.result and self.operands == other.operands

    def can_be_made_true(self) -> bool:
        if len(self.operands) == 1:
            return self.operands[0] == self.result

        two_first_operands = self.operands[:2]
        rest_of_operands = self.operands[2:]

        for operator in operators:
            new_operands = [operator(two_first_operands), *rest_of_operands]
            new_operation = Operation(
                result=self.result, operands=new_operands
            )
            if new_operation.can_be_made_true():
                return True

        return False


def parse_input(data: str) -> list[Operation]:
    data = data.strip("\n")

    operations = []
    for line in data.split("\n"):
        result_str, operands_str = line.split(": ")
        operations.append(
            Operation(
                result=int(result_str),
                operands=[
                    int(operand_str) for operand_str in operands_str.split(" ")
                ],
            )
        )

    return operations
