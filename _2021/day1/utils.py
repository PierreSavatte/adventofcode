from _2021 import aoc_utils


def parse_file(file_path):
    return aoc_utils.parse_file(
        file_path, line_parser=lambda x: int(x.strip("/n"))
    )
