def parse_instructions(instructions: str) -> list[int]:
    lines = instructions.strip().split("\n")
    return [int(line.replace("R", "").replace("L", "-")) for line in lines]


def rotate(start: int, amount: int, wheel_size: int = 100) -> int:
    return (start + amount) % wheel_size
