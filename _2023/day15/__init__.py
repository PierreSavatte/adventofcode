def compute_hash(string: str) -> int:
    current_value = 0
    for character in string:
        ascii_code = ord(character)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value
