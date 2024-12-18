from typing import Callable, Generator, Optional


class ReservedValue(Exception):
    ...


class HaltingProgram(Exception):
    ...


class Computer:
    def __init__(
        self,
        register_a: int,
        register_b: int,
        register_c: int,
        program: list[int],
    ):
        self.register_a = register_a
        self.register_b = register_b
        self.register_c = register_c
        self.program = program
        self.instruction_pointer = 0
        self.length_program = len(program)

        self.program_string = self.get_program_to_string(program)

    def copy(self) -> "Computer":
        return Computer(
            register_a=self.register_a,
            register_b=self.register_b,
            register_c=self.register_c,
            program=self.program[:],
        )

    @staticmethod
    def get_program_to_string(program: list[int]) -> str:
        return ",".join(map(str, program))

    def read(self) -> int:
        if self.instruction_pointer >= self.length_program:
            raise HaltingProgram()
        value = self.program[self.instruction_pointer]
        self.instruction_pointer += 1
        return value

    def to_combo_operand(self, literal_operand: int) -> int:
        operand_mapping = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.register_a,
            5: self.register_b,
            6: self.register_c,
        }

        value = operand_mapping.get(literal_operand)
        if value is None:
            raise ReservedValue(f"The operand {literal_operand} is reserved.")
        return value

    def _dv(self):
        literal_operand = self.read()
        combo_operand = self.to_combo_operand(literal_operand)
        return int(self.register_a / (2 ** combo_operand))

    def adv(self):
        value = self._dv()
        self.register_a = value

    def bxl(self):
        literal_operand = self.read()
        self.register_b = self.register_b ^ literal_operand

    def bst(self):
        literal_operand = self.read()
        combo_operand = self.to_combo_operand(literal_operand)
        self.register_b = combo_operand % 8

    def jnz(self):
        literal_operand = self.read()
        if self.register_a == 0:
            return
        self.instruction_pointer = literal_operand

    def bxc(self):
        literal_operand = self.read()  # For legacy reasons
        self.register_b = self.register_b ^ self.register_c

    def out(self) -> int:
        literal_operand = self.read()
        combo_operand = self.to_combo_operand(literal_operand)
        return combo_operand % 8

    def bdv(self):
        value = self._dv()
        self.register_b = value

    def cdv(self):
        value = self._dv()
        self.register_c = value

    def my_program(self, value: int) -> str:
        # Specific to my input

        # jnz
        result = []
        while value != 0:
            # bst
            register_b = value % 8

            # bxl
            register_b = register_b ^ 7

            # cdv
            register_c = value // (2 ** register_b)

            # bxl
            register_b = register_b ^ 7

            # bxc
            register_b = register_b ^ register_c

            # adv
            value = value // 8

            # out
            result.append(register_b % 8)

        return self.get_program_to_string(result)

    def to_instruction(self, opcode: int) -> Callable[[], Optional[int]]:
        opcode_instruction_mapping = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        return opcode_instruction_mapping[opcode]

    def step(self, debug: bool = False) -> Optional[int]:
        opcode = self.read()
        instruction = self.to_instruction(opcode)
        if debug:
            print(f"Running {instruction.__name__} ({opcode=})")
        return instruction()

    def print_state(self):
        print(
            f"register_a={self.register_a}, "
            f"register_b= {self.register_b}, "
            f"register_c= {self.register_c}"
        )

    def run(self, debug: bool = False) -> str:
        result = []
        halt = False
        while not halt:
            if debug:
                self.print_state()
            try:
                value = self.step(debug=debug)
            except HaltingProgram:
                halt = True
                value = None

            if value is not None:
                result.append(value)

        if debug:
            self.print_state()
        return self.get_program_to_string(result)

    def __repr__(self):
        return (
            f"Computer(register_a={self.register_a}, "
            f"register_b={self.register_b}, "
            f"register_c={self.register_c}, program={self.program})"
        )

    def __eq__(self, other: "Computer") -> bool:
        if not isinstance(other, Computer):
            raise NotImplementedError()

        return (
            self.register_a == other.register_a
            and self.register_b == other.register_b
            and self.register_c == other.register_c
            and self.program == other.program
        )


def parse_line(line: str) -> str:
    return line.split(": ")[-1]


def parse_input(data: str) -> Computer:
    data = data.strip("\n")

    registers_data, program_data = data.split("\n\n")
    register_a, register_b, register_c = [
        int(parse_line(line)) for line in registers_data.split("\n")
    ]

    program = [
        int(character) for character in parse_line(program_data).split(",")
    ]

    return Computer(
        register_a=register_a,
        register_b=register_b,
        register_c=register_c,
        program=program,
    )
