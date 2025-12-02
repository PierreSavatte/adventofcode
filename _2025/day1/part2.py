from _2025.day1 import parse_instructions, rotate
from _2025.load_input import load_input


class Safe:
    def __init__(self, dial: int = 50, wheel_size: int = 100):
        self.dial = dial
        self.number_of_times_dial_goes_to_0 = 0
        self.number_of_times_dial_ends_at_0 = 0
        self.wheel_size = wheel_size

    def execute(self, instruction: int):
        self.number_of_times_dial_goes_to_0 += (
            abs(instruction) // self.wheel_size
        )

        if self.dial != 0:
            rest = abs(instruction) % self.wheel_size
            has_passed_0_once = False
            if instruction > 0:
                has_passed_0_once = self.dial + rest > self.wheel_size
            elif instruction < 0:
                has_passed_0_once = self.dial - rest < 0
            if has_passed_0_once:
                self.number_of_times_dial_goes_to_0 += 1

        self.dial = rotate(self.dial, instruction, self.wheel_size)
        if self.dial == 0:
            self.number_of_times_dial_ends_at_0 += 1

    def execute_all(self, instructions: list[int]):
        for instruction in instructions:
            self.execute(instruction)

    def get_password(self) -> int:
        return (
            self.number_of_times_dial_goes_to_0
            + self.number_of_times_dial_ends_at_0
        )


def main():
    raw_instructions = load_input(1)
    safe = Safe()

    safe.execute_all(parse_instructions(raw_instructions))

    print(safe.get_password())


if __name__ == "__main__":
    main()
