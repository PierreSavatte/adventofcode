from dataclasses import dataclass

from _2023.load_input import load_input


@dataclass
class Game:
    id: int
    max_blue: int
    max_red: int
    max_green: int


def accept_game(
    game: Game, max_red: int, max_green: int, max_blue: int
) -> bool:
    for key, value in [
        ("max_red", max_red),
        ("max_green", max_green),
        ("max_blue", max_blue),
    ]:
        if getattr(game, key) > value:
            return False

    return True


def filter_games(
    games: list[Game],
    max_red: int = 12,
    max_green: int = 13,
    max_blue: int = 14,
) -> list[int]:
    return [
        game.id
        for game in games
        if accept_game(game, max_red, max_green, max_blue)
    ]


def parse_round(round: str) -> dict[str, int]:
    round_data = {}
    items_shown = round.split(", ")
    for item_shown in items_shown:
        number, item = item_shown.split(" ")
        round_data[item] = int(number)
    return round_data


def parse_line(line: str) -> Game:
    game_txt, game_data_txt = line.split(": ")
    game_id = int(game_txt.removeprefix("Game "))

    game_data = {}
    for round in game_data_txt.split("; "):
        round_data = parse_round(round)
        for item, number in round_data.items():
            key_in_game_data = f"max_{item}"
            value_in_game_data = game_data.get(key_in_game_data, 0)
            if value_in_game_data < number:
                game_data[key_in_game_data] = number

    return Game(id=game_id, **game_data)


def compute_answer(data: str) -> int:
    games = []
    for line in data.split("\n"):
        game = parse_line(line)
        games.append(game)

    games_ids = filter_games(games)

    return sum(games_ids)


if __name__ == "__main__":
    print(compute_answer(load_input(2)))
