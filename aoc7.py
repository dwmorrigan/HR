from stopwatch import Stopwatch
from itertools import product


def load_input(name):
    data = []
    with open(name) as f:
        for line in f:
            data.append(line.strip())
    return data


def make_dict(input_values):
    values = []
    for x in input_values:
        y, z = x.strip().split(':')
        target = int(y)
        members = list(map(int, z.strip().split()))
        values.append((target, members))
    return values


def find_good_equations(potential_equations, part2=False):
    calibration = 0
    for target, members in potential_equations:
        spots = len(members) - 1
        potentials = set()
        if part2:
            pattern = list(product([0, 1, 2], repeat=spots)) 
        else:
            pattern = list(product([0, 1], repeat=spots)) 
        # x is all of the patterns, q is this pattern
        for q in pattern:
            temp_val = members[0]
            for i, j in enumerate(q):
                if j == 0:
                    temp_val += members[i+1]
                elif j == 1:
                    temp_val *= members[i+1]
                else:
                    temp_val = int(str(temp_val) + str(members[i+1]))
            potentials.add(temp_val)
        if target in potentials:
            calibration += target
    return calibration


def main():
    sw = Stopwatch()
    sw.start()
    raw_test = load_input('aoc7.txt') # Input file
    puzzle = make_dict(raw_test)
    # Part 1
    sum_good_calibrations = find_good_equations(puzzle)
    print(sum_good_calibrations) # 1298103531759 181ms
    # Part 2
    sum_good_calibrations = find_good_equations(puzzle, part2=True)
    print(sum_good_calibrations) # 140575048428831 26s
    sw.stop()
    print(sw)


if __name__ == "__main__":
    main()
