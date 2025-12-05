from _2025.day3 import BaseBanks
from _2025.load_input import load_input


def pop_from_string(string: str, index: int) -> str:
    return string[:index] + string[index + 1 :]


class LargeBanks(BaseBanks):
    def get_bank_max_joltage(self, bank: str) -> int:
        nb_available_batteries = 12
        nb_batteries = len(bank)
        nb_banks_to_remove = nb_batteries - nb_available_batteries

        while nb_banks_to_remove > 0:
            has_removed_a_battery = False
            i = 0
            while i < len(bank) - 1:
                if int(bank[i]) < int(bank[i + 1]):
                    bank = pop_from_string(bank, i)
                    nb_banks_to_remove -= 1
                    has_removed_a_battery = True
                    break
                else:
                    i += 1

            while not has_removed_a_battery:
                for j in range(10):
                    if (index := bank.find(str(j))) != -1:
                        bank = pop_from_string(bank, index)
                        nb_banks_to_remove -= 1
                        has_removed_a_battery = True
                        break

        return int(bank)


def main():
    banks = LargeBanks(load_input(3))
    print(banks.get_total_joltage_output())


if __name__ == "__main__":
    main()
