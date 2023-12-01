def parse_file(file_path, line_parser):
    with open(file_path, "r") as fp:
        data = fp.readlines()

    parsed_values = list(map(line_parser, data))
    return parsed_values
