def parse_input(data: str) -> list[int]:
    data = data.strip("\n")

    return list(map(int, data.split(" ")))


def change_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        i = len(stone_str) // 2
        a, b = stone_str[:i], stone_str[i:]
        return [int(a), int(b)]

    new_stone = stone * 2024
    return [new_stone]


def change(stones: list[int]) -> list[int]:
    new_stones = []
    for stone in stones:
        new_stones.extend(change_stone(stone))
    return new_stones
