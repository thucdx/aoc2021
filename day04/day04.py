import os, re

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))

drawn = []
boards = []

input_path = "sample"

def print_board(cur_board):
    print("#####")
    for row in cur_board:
        print(" ".join(map(str, row)))
    print("#####")

with open("{0}/{1}".format(dir_path, input_path), "r") as f:
    drawn_line = f.readline()
    drawn = list(map(int, drawn_line.split(",")))

    # Read boards
    cur_board = []

    while True:
        line = f.readline()
        print("Line: ", line, len(line))
        if not line:
            if len(cur_board) > 0:
                boards.append(cur_board)
            break

        line = line.strip()
        print(line)
        if len(line) == 0:
            if len(cur_board) > 0:
                boards.append(cur_board)
            cur_board = []
        else:
            numbers = list(map(int, re.split("\s+", line)))

            cur_board.append(numbers)

    print('Drawn: ', drawn)
    print('Total board', len(boards))
    for board in boards:
        print_board(board)

def part_one():
    total_board = len(boards)
    board_flag = [[[[False] * 5] * 5] * total_board]

    for number in drawn:
        for i in range(total_board):
            cur_board = boards[i]
            bingo = False
            unmarked_sum = 0
            for j in range(5):
                for k in range(5):
                    if cur_board[j][k] == number:
                        board_flag[i][j][k] = True
                        # Check for bingo
                        # all row
                        if all(board_flag[i][j]):
                            bingo = True

                        # all column
                        bingo_by_col = True
                        for t in range(5):
                            if not board_flag[i][t][k]:
                                bingo_by_col = False
                                break
                        bingo |= bingo_by_col

                    if not board_flag[i][j][k]:
                        unmarked_sum += cur_board[j][k]

            if bingo:
                print("Final score: ", unmarked_sum * number)
                return

    print("Not found")

if __name__ == "__main__":
    part_one()