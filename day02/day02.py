import os

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = []

with open("{0}/input".format(dir_path), "r") as f:
    lines = f.readlines()


def part_one():
    horizontal = 0
    depth = 0

    for line in lines:
        parts = line.split(" ")
        cmd = parts[0]
        value = int(parts[1])

        if cmd == "forward":
            horizontal += value
        elif cmd == "up":
            depth -= value
        elif cmd == "down":
            depth += value

    print(horizontal, depth)
    print(horizontal * depth)


def part_two():
    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        parts = line.split(" ")
        cmd, value = parts[0], int(parts[1])

        if cmd == "forward":
            horizontal += value
            depth += aim * value
        elif cmd == "up":
            aim -= value
        elif cmd == "down":
            aim += value

    print(horizontal, depth)
    print(horizontal * depth)



if __name__ == "__main__":
    # part_one()
    part_two()
