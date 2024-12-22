def mix(secret_number: int, value: int) -> int:
    return secret_number ^ value


def prune(secret_number: int) -> int:
    return secret_number % 16777216


def generate_next_secret_number(previous_secret_number: int) -> int:
    secret_number = prune(
        mix(previous_secret_number, previous_secret_number * 64)
    )
    secret_number = prune(mix(secret_number, secret_number // 32))
    return prune(mix(secret_number, secret_number * 2048))



def parse_input(data: str) -> list[int]:
    data = data.strip("\n")
    return list(map(int, data.split("\n")))
