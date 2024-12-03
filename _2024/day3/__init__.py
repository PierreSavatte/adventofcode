import re


def parse_input(data: str, regex: str):
    data = data.strip()
    match = re.findall(regex, data)
    return [(int(a), int(b)) for a, b in match]
