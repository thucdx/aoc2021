import os

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = []

with open("{0}/input".format(dir_path), "r") as f:
    lines = f.readlines()

def part_one():
    res = 0
    last = None
    for line in lines:
        cur = int(line)
        if last is not None:
            if cur > last:
                res += 1
        last = cur

    print("Part one result: {0}".format(res))

def part_two():
    res = 0
    number = [int(line) for line in lines]
    last_sum = number[0] + number[1] + number[2]

    for i in range(1, len(number) - 2):
        cur_sum = number[i] + number[i+1] + number[i+2]
        res += cur_sum > last_sum
        last_sum = cur_sum

    print("Part two result: {0}".format(res))

if __name__ == "__main__":
    part_one()
    part_two()