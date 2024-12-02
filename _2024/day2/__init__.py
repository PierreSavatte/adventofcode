def parse_input(data: str) -> list[list[int]]:
    data = data.strip("\n")
    return [list(map(int, line.split())) for line in data.split("\n")]
