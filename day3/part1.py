FILE = "input"


def readlines(file):
    with open(file, "r") as fp:
        data = fp.readlines()
    return list(map(lambda x: x.strip("\n"), data))


def count_bit_occurrence(lines, index):
    nb_of_1 = 0
    nb_of_0 = 0
    for line in lines:
        if line[index] == "1":
            nb_of_1 += 1
        else:
            nb_of_0 += 1
    return nb_of_1, nb_of_0


def binary_to_integer(binary):
    return int(binary, base=2)


def resolution(file_path):
    lines = readlines(file_path)

    nb_bits = len(lines[0])

    gamma_binary = ""
    epsilon_binary = ""
    for bit_i_gamma in range(nb_bits):
        nb_of_1, nb_of_0 = count_bit_occurrence(lines, index=bit_i_gamma)
        if nb_of_1 > nb_of_0:
            gamma_binary += "1"
            epsilon_binary += "0"
        else:
            gamma_binary += "0"
            epsilon_binary += "1"

    gamma = binary_to_integer(gamma_binary)
    epsilon = binary_to_integer(epsilon_binary)

    return gamma * epsilon


def challenge_resolution():
    return resolution(FILE)


if __name__ == "__main__":
    print(challenge_resolution())
