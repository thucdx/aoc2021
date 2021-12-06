import os, re

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))

drawn = []
boards = []

input_path = "input"


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
            numbers = list(map(int, re.split('\\s+', line)))

            cur_board.append(numbers)

    print('Drawn: ', drawn)
    print('Total board', len(boards))
    for board in boards:
        print_board(board)


def first_board(boards):
    total_board = len(boards)
    board_flag = [[[False for _ in range(5)] for _ in range(5)] for _ in range(total_board)]

    for number in drawn:
        # print("Check for {0}".format(number))

        for i in range(total_board):
            cur_board = boards[i]
            cur_flag = board_flag[i]
            # print_board(cur_flag)
            # print("Shape {0} {1}".format(len(cur_flag), len(cur_flag[0])))
            bingo = False
            unmarked_sum = 0
            # print_board(cur_flag)
            for j in range(5):
                for k in range(5):
                    if cur_board[j][k] == number:
                        # print("Before assign ")
                        # print_board(cur_flag)
                        cur_flag[j][k] = True

                        # Check for bingo
                        bingo_by_row = all(cur_flag[j])
                        bingo_by_col = all([cur_flag[t][k] for t in range(5)])
                        # print_board(cur_flag)
                        # print_board([[cur_flag[t][k] for t in range(5)]])
                        bingo = bingo_by_row | bingo_by_col
                        if bingo:
                            print(i, j, k, bingo_by_row, bingo_by_col)

                    if not cur_flag[j][k]:
                        unmarked_sum += cur_board[j][k]

            if bingo:
                score = unmarked_sum * number
                print("Final score: {0}, unmarked_sum: {1}, number: {2}"
                      .format(unmarked_sum * number, unmarked_sum, number))
                return i, score

    print("Not found")
    return -1, 0


def part_one():
    first_board(boards)


def part_two():
    while len(boards) > 0:
        index, score = first_board(boards)
        boards.pop(index)

        if len(boards) == 0:
            print("Part two final score: {0}".format(score))


if __name__ == "__main__":
    part_two()
