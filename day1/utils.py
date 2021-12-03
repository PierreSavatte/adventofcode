def parse_file(file_path):
    with open(file_path, "r") as fp:
        data = fp.readlines()

    parsed_values = list(map(lambda x: int(x.strip("/n")), data))
    return parsed_values
