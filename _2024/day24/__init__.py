import operator
from dataclasses import dataclass
from enum import Enum
from typing import Callable

ADDRESS = str


class Operation(Enum):
    XOR = "XOR"
    OR = "OR"
    AND = "AND"

    def to_function(self) -> Callable[[bool, bool], bool]:
        mapping = {
            Operation.XOR: operator.xor,
            Operation.OR: operator.or_,
            Operation.AND: operator.and_,
        }
        return mapping[self]


@dataclass
class Gate:
    operation: Operation
    inputs: list[ADDRESS]
    output: ADDRESS


@dataclass
class Computer:
    data: dict[ADDRESS, bool]
    gates: list[Gate]

    def run(self):
        gates_to_perform = self.gates[:]
        while gates_to_perform:
            gate = gates_to_perform.pop(0)
            try:
                input_data = [self.data[address] for address in gate.inputs]
            except KeyError:
                gates_to_perform.append(gate)
                continue

            output_address = gate.output
            f = gate.operation.to_function()
            output_data = f(*input_data)
            self.data[output_address] = output_data

    def read_output(self) -> int:
        output_addresses = sorted(
            filter(starts_with_z, self.data.keys()), reverse=True
        )
        values = [
            self.data[output_address] for output_address in output_addresses
        ]
        str_values = list(map(lambda x: str(int(x)), values))
        return int("".join(str_values), 2)

    def copy(self) -> "Computer":
        return Computer(
            data=self.data.copy(),
            gates=self.gates[:],
        )


def starts_with_z(address: ADDRESS) -> bool:
    return address.startswith("z")


def parse_input(data: str) -> Computer:
    data = data.strip("\n")
    init_data, gates_data = data.split("\n\n")

    computer_data = {}
    for init_value in init_data.split("\n"):
        address, value = init_value.split(": ")
        computer_data[address] = bool(int(value))

    gates = []
    for gate_data in gates_data.split("\n"):
        operation_data, output = gate_data.split(" -> ")
        input_a, operation_str, input_b = operation_data.split(" ")
        gates.append(
            Gate(
                operation=Operation(operation_str),
                inputs=[input_a, input_b],
                output=output,
            )
        )

    return Computer(data=computer_data, gates=gates)
