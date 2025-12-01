from _2025.load_input import load_input


def parse_instructions(instructions: str) -> list[int]:
    lines = instructions.strip().split("\n")
    return [int(line.replace("R", "").replace("L", "-")) for line in lines]


def rotate(start: int, amount: int, wheel_size: int = 100) -> int:
    return (start + amount) % wheel_size


def compute_number_of_times_the_dial_points_to_value(
    dial: int, instructions: str, value: int
) -> int:
    counter = 0
    for rotation_amount in parse_instructions(instructions):
        dial = rotate(dial, rotation_amount)
        if dial == value:
            counter += 1
    return counter


def main():
    instructions = load_input(1)
    print(
        compute_number_of_times_the_dial_points_to_value(
            dial=50,
            instructions=instructions,
            value=0,
        )
    )


if __name__ == "__main__":
    main()
