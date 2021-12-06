import os

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))

input_path = "input"
lines = []

with open("{0}/{1}".format(dir_path, input_path), "r") as f:
    lines = f.readlines()


def part_one():
    board_size = 1000
    cnt = [[0 for _ in range(board_size)] for _ in range(board_size)]
    max_num = 1

    for line in lines:
        parts = line.split("->")
        x1, y1 = list(map(int, parts[0].split(",")))
        x2, y2 = list(map(int, parts[1].split(",")))

        # print(x1, y1, '->', x2, y2)
        max_num = max(max_num, max([x1, y1, x2, y2]))

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                cnt[x1][i] += 1

        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                cnt[i][y1] += 1

    print(max_num)
    res = 0
    for i in range(max_num + 1):
        for j in range(max_num + 1):
            res += cnt[i][j] >= 2
    print("Total ", res)


def part_two():
    board_size = 1000
    cnt = [[0 for _ in range(board_size)] for _ in range(board_size)]
    max_num = 1

    for line in lines:
        parts = line.split("->")
        x1, y1 = list(map(int, parts[0].split(",")))
        x2, y2 = list(map(int, parts[1].split(",")))

        # print(x1, y1, '->', x2, y2)
        max_num = max(max_num, max([x1, y1, x2, y2]))

        dx = x2 - x1
        dy = y2 - y1
        k = max(abs(dx), abs(dy))

        step_x = dx // k
        step_y = dy // k

        for i in range(0, k+1):
            x = x1 + step_x * i
            y = y1 + step_y * i
            cnt[x][y] += 1

    print(max_num)
    res = 0
    for i in range(max_num + 1):
        for j in range(max_num + 1):
            res += cnt[i][j] >= 2
    print("Total ", res)


if __name__ == "__main__":
    part_two()
