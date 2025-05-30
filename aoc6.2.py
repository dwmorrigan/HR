from stopwatch import Stopwatch

def load_input(name):
    data = []
    with open(name) as f:
        for line in f:
            data.append(line.strip())
    return data

'''
Take the raw data and process it to find the starting point and all blocks (bounces).
'''
def graph(raw_test):
    bounce = set()
    start = ()
    for x in range(len(raw_test)):
        for y in range(len(raw_test[0])):
            if raw_test[x][y] == '^':
                start = (x, y)
            if raw_test[x][y] == '#':
                bounce.add((x, y))
    packed = [start, bounce]
    return packed

'''
With the starting position and the obstacles (and outer limits), find the path that will lead to exiting the "maze"
'''
def path(home, obstacles, xlimit, ylimit):
    x, y = home
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    d = 0
    dir = dirs[d]
    path = []
    keep_going = True
    while keep_going:
        while (x, y) not in obstacles and x >= 0 and x < xlimit and y >= 0 and y < ylimit:
            path.append([x,y,d])
            x += dir[0]
            y += dir[1]
        if x < 0 or x >= xlimit or y < 0 or y >= ylimit:
            keep_going = False
        x -= dir[0]
        y -= dir[1]
        d = (d+1) % 4
        dir = dirs[d]
        x += dir[0]
        y += dir[1]
    return path

'''
Slightly obnoxious (there must be a better) way to find how many places a single new obstacle will cause the "maze" to never be completed - a.k.a it loops. Only locations that are found on the original path are considered because the un-pathed locations will never be reached without the new obstacles. Each new obstacle may or may not create a loop, so check each new set of obstacles, one by one, to find those that do create loops. 
'''
def find_loops(new_obstacle, home, obstacles, xlimit, ylimit):
    obstacles.add(new_obstacle)
    x, y = home
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    d = 0
    dir = dirs[d]
    path = list()
    count = 0
    keep_going = True
    while keep_going:
        while (x, y) not in obstacles and x >= 0 and x <= xlimit and y >= 0 and y <= ylimit:
            if [x,y,d] in path:
                count = count + 1
                if count > 4:
                    obstacles.remove(new_obstacle)
                    return new_obstacle
            path.append([x,y,d])
            x += dir[0]
            y += dir[1]
        if x < 0 or x >= xlimit or y < 0 or y >= ylimit:
            keep_going = False
        x -= dir[0]
        y -= dir[1]
        d = (d+1) % 4
        dir = dirs[d]
        x += dir[0]
        y += dir[1]
    obstacles.remove(new_obstacle)
    return 0


def main():
    sw = Stopwatch()
    sw.start()
    raw_test = load_input('aoc6.1.txt') # Input file
    row = len(raw_test)
    col = len(raw_test[0])
    init, blocks = graph(raw_test) # Find starting point and obstacles
    tao = path(init, blocks, row, col) # Find the path that leads to an exit
    count = set()
    for each in tao[1:]: # Take each step of the path (except for the starting location)
        t_each = tuple(each)
        beep = find_loops(t_each[:-1], init, blocks, row, col) # And add that step to the obstacles list to find a new path that either A> exits or B> loops. 
        if beep != 0:
            count.add(beep) # Add the looping obstacles to a set (so that duplicates are not recorded)
    print(len(count)) # Part 2: 1655 
    sw.stop()
    print(sw) # 6 minutes and 26 seconds. . . !!

if __name__ == "__main__":
    main()
