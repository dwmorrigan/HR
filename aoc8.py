#!usr/bin/env python

from collections import defaultdict
from itertools import combinations as cc


def load_data(fn):
    data = []
    with open(fn) as f:
        for line in f:
            data.append(line.strip())
    return data


def process_data(raw_data):
    antenna_locations = defaultdict(list)
    for i in range(len(raw_data)):
        for j in range(len(raw_data[0])):
            if raw_data[i][j] == '.':
                continue
            antenna_locations[raw_data[i][j]].append((i, j))
    return antenna_locations


def find_antinodes(antennas, limit):
    antinodes = set()
    for k, v in antennas.items():
        vv = cc(v, 2)
        for each_pair in vv:
            x1, y1 = each_pair[0]
            x2, y2 = each_pair[1]
            stepx = x2-x1
            stepy = y2-y1
            if x1-stepx >= 0 and x1-stepx < limit and y1-stepy >=0 and y1-stepy < limit:
                antinodes.add((x1-stepx, y1-stepy))
            if x2+stepx >= 0 and x2+stepx < limit and y2+stepy >= 0 and y2+stepy < limit:
                antinodes.add((x2+stepx, y2+stepy))
    print(len(antinodes))


def find_antinode_lines(antennas, limit):
    antinodes = set()
    for k, v in antennas.items():
        vv = cc(v, 2)
        for each_pair in vv:
            x1, y1 = each_pair[0]
            x2, y2 = each_pair[1]
            antinodes.add((x1, y1))
            antinodes.add((x2, y2))
            offset_x = x2-x1
            offset_y = y2-y1
            stepx = offset_x
            stepy = offset_y
            while x1-stepx >= 0 and x1-stepx < limit and y1-stepy >= 0 and y1-stepy < limit:
                antinodes.add((x1-stepx, y1-stepy))
                stepx += offset_x
                stepy += offset_y
            stepx = offset_x
            stepy = offset_y
            while x2+stepx >= 0 and x2+stepx < limit and y2+stepy >= 0 and y2+stepy < limit:
                antinodes.add((x2+stepx, y2+stepy))
                stepx += offset_x
                stepy += offset_y
    print(len(antinodes))


def main():
    test = "aoc8.txt"
    matrix = load_data(test)
    locations = process_data(matrix)
    limit = max(len(matrix), len(matrix[0]))
    find_antinodes(locations, limit) # Part 1: 381
    find_antinode_lines(locations, limit) # Part 2: 1184


if __name__ == "__main__":
    main()