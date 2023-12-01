from pathlib import Path

CURRENT_FOLDER = Path(__file__).parent.resolve()


def load_input(day: int) -> str:
    with open(Path(CURRENT_FOLDER, f"day{day}", "input"), "r") as fp:
        data = fp.read()
    return data
