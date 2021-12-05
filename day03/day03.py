import os

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
lines = []

with open("{0}/input".format(dir_path), "r") as f:
    lines = [line.strip() for line in f.readlines()]


def part_one():
    total = len(lines)
    code_length = len(lines[0])
    cnt_zero = [0] * code_length
    print(code_length)

    for line in lines:
        for i in range(code_length):
            if line[i] == '0':
                cnt_zero[i] += 1

    gamma_rate_str = ""
    for i in range(code_length):
        if 2 * cnt_zero[i] > total:
            gamma_rate_str += '0'
        else:
            gamma_rate_str += '1'

    print(gamma_rate_str)
    gamma_rate = int(gamma_rate_str, 2)
    epsilon_rate = 2 ** code_length - 1 - gamma_rate
    print(gamma_rate, epsilon_rate)
    print("Power consumption is: ", gamma_rate * epsilon_rate)


def oxygen_criteria(zero_arr, one_arr):
    if len(zero_arr) > len(one_arr):
        return zero_arr
    else:
        return one_arr

def scrubber_criteria(zero_arr, one_arr):
    if len(zero_arr) > len(one_arr):
        return one_arr
    else:
        return zero_arr

def find_rating(logs, chooseFunc):
    cur_bit_pos = 0
    while len(logs) > 1:
        zero_bit = []
        one_bit = []
        for log in logs:
            if log[cur_bit_pos] == '0':
                zero_bit.append(log)
            else:
                one_bit.append(log)

        # Remove
        logs = chooseFunc(zero_bit, one_bit)
        cur_bit_pos = cur_bit_pos + 1

    return logs[0]


def part_two():
    oxygen_generator_rating = find_rating(lines, oxygen_criteria)
    print("Oxygen generator rating", oxygen_generator_rating)

    co2_scrubber_rating = find_rating(lines, scrubber_criteria)
    print("CO2 scrubber rating", co2_scrubber_rating)

    print("Life support rating", int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))


if __name__ == "__main__":
    part_two()
