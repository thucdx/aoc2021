import os

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))

input_path = "input"
lines = []

with open("{0}/{1}".format(dir_path, input_path), "r") as f:
    lines = f.readlines()
    fishes = list(map(int, lines[0].split(",")))
    cycle = 7
    mature = 2

def part_one(total_day=80):
    print("Fishes: ", " ".join(map(str, fishes)))

    for day in range(1, total_day+1):
        new_fishes = []
        for i in range(len(fishes)):
            if fishes[i] == 0:
                new_fishes.append(cycle + mature - 1)
                fishes[i] = cycle - 1
            else:
                fishes[i] -= 1

        fishes.extend(new_fishes)
        # print("Day {0}: {1}".format(day, " ".join(map(str, fishes))))
        print("Day {0}, total {1}".format(day, len(fishes)))

    print("Total fishes: {0}".format(len(fishes)))


def part_two(total_day=256):
    cnt = [[0 for _ in range(cycle + mature)] for _ in range(260)]

    for fish in fishes:
        cnt[0][fish] += 1
    print("Day 0: {0}".format(" ".join(map(str, cnt[0]))))

    for day in range(1, total_day+1):
        for counter in range(0, cycle + mature-1):
            # calculate cnt[day][counter]
            cnt[day][counter] = cnt[day-1][counter+1]

        # new-born
        cnt[day][cycle + mature - 1] = cnt[day-1][0]
        # new cycle
        cnt[day][cycle - 1] += cnt[day-1][0]

        total = sum(cnt[day])
        print("Day {0}: {1}".format(day, " ".join(map(str, cnt[day]))))
        print("Day {0}, total {1}".format(day, total))


if __name__ == "__main__":
    part_two(256)
