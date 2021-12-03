FILE = "input"


def resolution(series):
    series_copy = series[:]

    last_item = series_copy.pop(0)
    nb_increased = 0
    for item in series_copy:
        if item > last_item:
            nb_increased += 1

        last_item = item

    return nb_increased


def parse_file(file_path):
    with open(file_path, "r") as fp:
        data = fp.readlines()

    parsed_values = list(map(lambda x: int(x.strip("/n")), data))
    return parsed_values


def challenge_resolution():
    series = parse_file(FILE)
    return resolution(series)


if __name__ == "__main__":
    print(challenge_resolution())
