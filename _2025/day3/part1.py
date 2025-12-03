from _2025.day3 import BaseBanks
from _2025.load_input import load_input


class SimpleBanks(BaseBanks):
    def get_bank_max_joltage(self, bank: str) -> int:
        for a in range(9, -1, -1):
            i = bank.find(str(a))
            if i == -1:
                continue

            sub_bank = bank[i + 1 :]
            for b in range(9, -1, -1):
                j = sub_bank.find(str(b))
                if j == -1:
                    continue

                return int(f"{a}{b}")
        return 0


def main():
    banks = SimpleBanks(load_input(3))
    print(banks.get_total_joltage_output())


if __name__ == "__main__":
    main()
