from _2021.day4.part1 import parse_file, compute_score, check_board_won

FILE = "input"

NB_COL = 5
NB_LINES = 5


def resolution(drawn_numbers, boards):
    nb_boards = len(boards)
    # Draw numbers
    for drawn_number in drawn_numbers:
        i_board = 0
        while i_board < nb_boards:

            # Mark board
            board = boards[i_board]
            for x in range(NB_COL):
                for y in range(NB_LINES):
                    if board[x][y] == drawn_number:
                        board[x][y] = None

            if check_board_won(board):
                boards.pop(i_board)
                nb_boards -= 1
                if nb_boards == 0:
                    return compute_score(board, drawn_number)
            else:
                i_board += 1


def challenge_resolution():
    drawn_numbers, boards = parse_file(FILE)
    return resolution(drawn_numbers, boards)


if __name__ == "__main__":
    print(challenge_resolution())
