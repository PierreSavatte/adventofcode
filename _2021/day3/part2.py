from _2021.day3.part1 import readlines, count_bit_occurrence, binary_to_integer

FILE = "input"


def keep_only_binaries_by_value_at_index(binaries, value, index):
    filtered_binaries = []
    for binary in binaries:
        if binary[index] == value:
            filtered_binaries.append(binary)
    return filtered_binaries


def apply_bit_criteria(lines, nb_bits, comparator):
    for bit_index in range(nb_bits):

        nb_of_1, nb_of_0 = count_bit_occurrence(lines, bit_index)
        if comparator(nb_of_1, nb_of_0):
            bit_to_keep = "1"
        else:
            bit_to_keep = "0"

        lines = keep_only_binaries_by_value_at_index(
            lines, value=bit_to_keep, index=bit_index
        )

        if len(lines) == 1:
            return lines[0]


def resolution(file_path):
    all_lines = readlines(file_path)

    nb_bits = len(all_lines[0])

    oxygen_generator_rating_binary = apply_bit_criteria(
        all_lines[:],
        nb_bits=nb_bits,
        comparator=lambda nb_of_1, nb_of_0: nb_of_1 >= nb_of_0,
    )

    co2_scrubber_rating_binary = apply_bit_criteria(
        all_lines[:],
        nb_bits=nb_bits,
        comparator=lambda nb_of_1, nb_of_0: nb_of_1 < nb_of_0,
    )

    oxygen_generator_rating = binary_to_integer(oxygen_generator_rating_binary)
    co2_scrubber_rating = binary_to_integer(co2_scrubber_rating_binary)

    return oxygen_generator_rating * co2_scrubber_rating


def challenge_resolution():
    return resolution(FILE)


if __name__ == "__main__":
    print(challenge_resolution())
