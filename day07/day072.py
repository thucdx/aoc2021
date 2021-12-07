import os

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))

input_path = "input"
lines = []
position = []

with open("{0}/{1}".format(dir_path, input_path), "r") as f:
    lines = f.readlines()


def fuel_spend(cost_func=lambda crab, pos: abs(crab - pos)):
    crabs = list(map(int, lines[0].split(",")))
    cost = [0] * (5 + max(crabs))
    for crab in crabs:
        for i in range(len(cost)):
            cost[i] += cost_func(crab, i)

    min_value = (5 + max(crabs))**4
    min_index = -1
    for i in range(len(cost)):
        cur_cost = cost[i]
        if cur_cost < min_value:
            min_value = cur_cost
            min_index = i

    print(min_index, min_value)


def part_one():
    fuel_spend()


def part_two():
    def cost_function(crab, position):
        distance = abs(crab - position)
        return distance*(distance+1)/2

    fuel_spend(cost_function)


if __name__ == "__main__":
    # part_one()
    part_two()