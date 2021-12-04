import aoc_utils

FILE = "input"

NB_COL = 5
NB_LINES = 5


def _parse_line(raw_line, split):
    return [int(number) for number in raw_line.split(split) if number]


def parse_drawn_numbers(raw_drawn_numbers):
    return _parse_line(raw_drawn_numbers, split=",")


def parse_board_line(board_line):
    return _parse_line(board_line, split=" ")


def parse_file(file_path):

    data = aoc_utils.parse_file(file_path, line_parser=lambda x: x.strip("\n"))

    drawn_numbers = parse_drawn_numbers(data.pop(0))

    # Pop empty line after the drawn_numbers line
    data.pop(0)

    boards = []
    board = []
    for line in data:
        if line == "":
            boards.append(board)
            board = []
        else:
            parsed_line = parse_board_line(line)
            board.append(parsed_line)
    # Append last board to the board list
    boards.append(board)

    return drawn_numbers, boards


def check_board_won(board):
    # Check lines
    for line in board:
        if not [item for item in line if item]:
            return True

    # Check columns
    for y in range(NB_LINES):
        if not [x for x in range(NB_COL) if board[x][y]]:
            return True


def compute_score(board, drawn_number):
    total_score = 0
    for x in range(NB_COL):
        for y in range(NB_LINES):
            value = board[x][y]
            if value:
                total_score += value

    return total_score * drawn_number


def resolution(drawn_numbers, boards):
    # Draw numbers
    for drawn_number in drawn_numbers:
        for board in boards:

            # Mark board
            for x in range(NB_COL):
                for y in range(NB_LINES):
                    if board[x][y] == drawn_number:
                        board[x][y] = None

            if check_board_won(board):
                return compute_score(board, drawn_number)


def challenge_resolution():
    drawn_numbers, boards = parse_file(FILE)
    return resolution(drawn_numbers, boards)


if __name__ == "__main__":
    print(challenge_resolution())
