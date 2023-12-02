from _2023.day2.part1 import Game, parse_line
from _2023.load_input import load_input


def compute_power_of_game(game: Game) -> int:
    return game.max_red * game.max_blue * game.max_green


def compute_answer(data: str) -> int:
    games = []
    for line in data.split("\n"):
        game = parse_line(line)
        games.append(game)

    return sum(compute_power_of_game(game) for game in games)


if __name__ == "__main__":
    print(compute_answer(load_input(2)))
