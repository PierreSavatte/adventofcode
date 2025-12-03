class BaseBanks:
    def __init__(self, input: str = ""):
        self.banks = parse_input(input)

    def get_bank_max_joltage(self, bank: str) -> int:
        ...

    def get_total_joltage_output(self) -> int:
        return sum(self.get_bank_max_joltage(bank) for bank in self.banks)


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()
