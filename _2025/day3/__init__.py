from tqdm import tqdm


class BaseBanks:
    def __init__(self, input: str = ""):
        self.banks = parse_input(input)

    def get_bank_max_joltage(self, bank: str) -> int:
        ...

    def get_total_joltage_output(self) -> int:
        accumulator = 0
        progress_bar = tqdm(total=len(self.banks))
        for bank in self.banks:
            accumulator += self.get_bank_max_joltage(bank)
            progress_bar.update()
        progress_bar.close()
        return accumulator


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()
