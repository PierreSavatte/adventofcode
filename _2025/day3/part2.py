from itertools import combinations

from _2025.day3 import BaseBanks
from _2025.load_input import load_input


class LargeBanks(BaseBanks):
    def get_bank_max_joltage(self, bank: str) -> int:
        max = 0
        for combination in combinations(bank, 12):
            current = int("".join(combination))
            if current > max:
                max = current
        return max


def main():
    banks = LargeBanks(load_input(3))
    print(banks.get_total_joltage_output())


if __name__ == "__main__":
    main()
