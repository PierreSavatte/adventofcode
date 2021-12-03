FILE = "input"


def readlines(file):
    with open(file, "r") as fp:
        data = fp.readlines()
    return list(map(lambda x: x.strip("\n"), data))


def resolution(file_path):
    lines = readlines(file_path)

    nb_bits = len(lines[0])

    nb_of_1 = {i: 0 for i in range(nb_bits)}
    nb_of_0 = {i: 0 for i in range(nb_bits)}
    for line in lines:
        for bit_i in range(len(line)):
            if line[bit_i] == "1":
                nb_of_1[bit_i] += 1
            else:
                nb_of_0[bit_i] += 1

    gamma_binary = ""
    epsilon_binary = ""
    for bit_i_gamma in range(nb_bits):
        if nb_of_1[bit_i_gamma] > nb_of_0[bit_i_gamma]:
            gamma_binary += "1"
            epsilon_binary += "0"
        else:
            gamma_binary += "0"
            epsilon_binary += "1"

    gamma = int(gamma_binary, base=2)
    epsilon = int(epsilon_binary, base=2)

    return gamma * epsilon


def challenge_resolution():
    return resolution(FILE)


if __name__ == "__main__":
    print(challenge_resolution())
