'''
Rule #1 : Blocked arrow (guard) turns right
Rule #2: Not blocked arrow (guard) steps forward
Find # of distinct positions the guard visits before exiting the stage
'''


def load_input(name):
    data = []
    with open(name) as f:
        for line in f:
            data.append(line.strip())
    return data


def distinct(location):
    if location != 'X':
        return 1
    return 0


def transmute(raw_input):
    test = raw_input
    ttest = []
    for i, x in enumerate(test):
        ttest.append([])
        for j, y in enumerate(x):
            ttest[i].append(y)
            if y == '^':
                guard = [i, j, 0]
            elif y == '>':
                guard = [i, j, 1]
            elif y == 'v':
                guard = [i, j, 2]
            elif y == '<':
                guard = [i, j, 3]
    packed = [ttest, guard]
    return packed


def traverse(ttest, guard):
    exit = False
    counter = 0
    while exit is False:
        x, y, d = guard
        if d == 2:
            # check for exit
            if x+1 >= len(ttest):
                counter += distinct(ttest[x][y])
                ttest[x][y] = 'X'
                print(f"[{x}, {y}, {d}],", end=' ')
                exit = True
                break
            # check south
            if ttest[x+1][y] == '#':
                guard[2] = 3
            else:
                counter += distinct(ttest[x][y])
                ttest[x][y] = 'X'
                print(f"[{x}, {y}, {d}],", end=' ')
                guard[0] = x+1
        elif d == 1:
            # check for exit
            if y+1 >= len(ttest[0]):
                counter += distinct(ttest[x][y])
                ttest[x][y] = 'X'
                print(f"[{x}, {y}, {d}],", end=' ')
                exit = True
                break
            # check east
            if ttest[x][y+1] == '#':
                guard[2] = 2
            else:
                counter += distinct(ttest[x][y])
                ttest[x][y] = 'X'
                print(f"[{x}, {y}, {d}],", end=' ')
                guard[1] = y+1
        elif d == 0:
            # check for exit
            if x-1 < 0:
                counter += distinct(ttest[x][y])
                ttest[x][y] = 'X'
                print(f"[{x}, {y}, {d}],", end=' ')
                exit = True
                break
            # check north
            if ttest[x-1][y] == '#':
                guard[2] = 1
            else:
                counter += distinct(ttest[x][y])
                ttest[x][y] = 'X'
                print(f"[{x}, {y}, {d}],", end=' ')
                guard[0] = x-1
        elif d == 3:
            # check for exit
            if y-1 < 0:
                counter += distinct(ttest[x][y])
                ttest[x][y] = 'X'
                print(f"[{x}, {y}, {d}],", end=' ')
                exit = True
                break
            # check west
            if ttest[x][y-1] == '#':
                guard[2] = 0
            else:
                counter += distinct(ttest[x][y])
                ttest[x][y] = 'X'
                print(f"[{x}, {y}, {d}],", end=' ')
                guard[1] = y-1
        else:
            # something went wrong
            print("No")
    return counter


def main():
    raw_test = load_input('aoc6.txt')
    maze, facing = transmute(raw_test)
    print(traverse(maze, facing)) # Part 1: 4883


if __name__ == "__main__":
    main()
