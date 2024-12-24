import math
import operator
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from functools import cached_property, partial
from itertools import permutations
from typing import Callable

from tqdm import tqdm

ADDRESS = str


class Unsolvable(Exception):
    ...


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

    @property
    def _key(self):
        return (*self.inputs, self.operation.value, self.output)

    def __hash__(self):
        return hash(self._key)

    def __eq__(self, other):
        return self._key == other._key


@dataclass
class Computer:
    data: dict[ADDRESS, bool]
    gates: list[Gate]

    @cached_property
    def x(self) -> int:
        addresses = self.get_addresses_starting_with_char("x")
        return self.read_binary_to_int(addresses)

    @cached_property
    def y(self) -> int:
        addresses = self.get_addresses_starting_with_char("y")
        return self.read_binary_to_int(addresses)

    @cached_property
    def expected_result(self) -> int:
        return self.x + self.y

    def run(self):
        gates_to_perform = self.gates[:]
        skipped_gates = []
        while gates_to_perform:
            gate = gates_to_perform.pop(0)
            try:
                input_data = [self.data[address] for address in gate.inputs]
            except KeyError:
                gates_to_perform.append(gate)
                skipped_gates.append(gate)
                if len(skipped_gates) == len(gates_to_perform):
                    raise Unsolvable()
                continue

            output_address = gate.output
            f = gate.operation.to_function()
            output_data = f(*input_data)
            self.data[output_address] = output_data
            skipped_gates = []

    def read_binary_to_int(self, addresses: list[ADDRESS]) -> int:
        values = [self.data[address] for address in addresses]
        str_values = list(map(lambda x: str(int(x)), values))
        return int("".join(str_values), 2)

    def get_addresses_starting_with_char(
        self, character: str
    ) -> list[ADDRESS]:
        starts_with_my_char = partial(starts_with_char, character=character)
        addresses = sorted(
            filter(starts_with_my_char, self.data.keys()), reverse=True
        )
        return addresses

    def read_output(self) -> int:
        output_addresses = self.get_addresses_starting_with_char("z")
        return self.read_binary_to_int(output_addresses)

    def copy(self) -> "Computer":
        return deepcopy(self)

    def get_faulty_final_gates(self) -> list[Gate]:
        new_computer = self.copy()
        new_computer.run()
        expected_binary = int_to_bin(self.expected_result)
        result = int_to_bin(new_computer.read_output())

        incorrect_final_nodes = []
        i = len(result)
        for a, b in zip(expected_binary, result):
            if a != b:
                incorrect_final_nodes.append(f"z{i:02}")
            i -= 1

        faulty_final_gates = filter(
            lambda gate: gate.output in incorrect_final_nodes, self.gates
        )
        return list(faulty_final_gates)

    def get_gates_related_to(self, gate: Gate) -> set[Gate]:
        related_gates = {gate}
        for parent_address in gate.inputs:
            if parent_address.startswith("x") or parent_address.startswith(
                "y"
            ):
                continue
            for other_gate in self.gates:
                if other_gate.output == parent_address:
                    related_gates.update(self.get_gates_related_to(other_gate))
        return related_gates

    def swipe_cables(self, current_output: ADDRESS, new_output: ADDRESS):
        for gate in self.gates:
            if gate.output == current_output:
                gate.output = new_output
                return

    def get_cables_to_swipe(self) -> list[ADDRESS]:
        expected_result = self.expected_result

        faulty_gates = set()
        faulty_final_gates = self.get_faulty_final_gates()
        print("There are", len(faulty_final_gates), "faulty final gates")
        for final_gate in self.get_faulty_final_gates():
            faulty_gates.update(self.get_gates_related_to(final_gate))

        faulty_gates = list(faulty_gates)
        nb_faulty_gates = len(faulty_gates)
        print("There are a total of", nb_faulty_gates, "faulty gates.")

        nb_permutations = int(
            math.factorial(nb_faulty_gates)
            / math.factorial(nb_faulty_gates - 4)
        )
        progress_bar = tqdm(total=nb_permutations)
        for a, b, c, d in permutations(faulty_gates, 4):
            new_computer = self.copy()
            current_outputs = [a.output, b.output, c.output, d.output]
            new_outputs = [b.output, a.output, d.output, c.output]
            for current_output, new_output in zip(
                current_outputs, new_outputs
            ):
                new_computer.swipe_cables(current_output, new_output)

            try:
                new_computer.run()
            except Unsolvable:
                continue
            if new_computer.read_output() == expected_result:
                return sorted(new_outputs)

            progress_bar.update()
        progress_bar.close()

        raise Unsolvable(
            "No solution was found to compute the sum from x and y with any "
            "permutations of the wires."
        )


def starts_with_char(address: ADDRESS, character: str) -> bool:
    return address.startswith(character)


def int_to_bin(value: int) -> str:
    return "{0:b}".format(value)


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
