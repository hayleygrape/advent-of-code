import re
from itertools import combinations

from utils.get_input import get_inputs, get_year_and_day
from utils.common import *

def get_antenna_locs(f):
    ant_locs = {}
    for row in range(len(f)):
        for match in re.finditer(r'[a-zA-Z0-9]', f[row]):
            col = match.span()[0]
            char = f[row][col] 
            if char not in ant_locs:
                ant_locs[char] = []
            ant_locs[char].append((row,col))
    return ant_locs

def get_antinode_locs(cord1, cord2):
    rise, run = cord2[0]-cord1[0], cord2[1]-cord1[1]
    loc1 = (cord1[0]-rise, cord1[1]-run)
    loc2 = (cord2[0]+rise, cord2[1]+run)
    return loc1,loc2

def is_valid_cord(cord, row_len, col_len):  # written in (y,x)
    if cord[0] >= row_len or cord[0] < 0 or cord[1] >= col_len or cord[1] < 0:
        return False
    return True

def get_all_antinode_locs(cord1, cord2, col_len):
    locs = []
    m = (cord2[0]-cord1[0])/(cord2[1]-cord1[1])
    b = cord1[0]-(m*cord1[1])
    for x in range(col_len):
        y = round((m*x)+b,10)
        if y % 1 == 0:
            locs.append((y,x))
    return locs

def part1(b):
    ant_locs = get_antenna_locs(b)
    row_len, col_len = len(b), len(b[0])
    antinode_locs2 = set()
    for k,v in ant_locs.items():
        for cord1, cord2 in list(combinations(ant_locs[k], 2)):
            locs = get_all_antinode_locs(cord1, cord2, col_len)
            for loc in locs:
                if is_valid_cord(loc, row_len, col_len):
                    antinode_locs2.add(loc)
    return len(antinode_locs2)

def part2(b):
    ant_locs = get_antenna_locs(b)
    row_len, col_len = len(b), len(b[0])
    antinode_locs = set()
    for k,v in ant_locs.items():
        for cord1, cord2 in list(combinations(ant_locs[k], 2)):
            loc1, loc2 = get_antinode_locs(cord1, cord2)
            if is_valid_cord(loc1, row_len, col_len):
                antinode_locs.add(loc1)
            if is_valid_cord(loc2, row_len, col_len):
                antinode_locs.add(loc2)
    return len(antinode_locs)

if __name__=='__main__':
    puzzle_input, test_input = get_inputs(__file__)

    # testing part
    p1_ans_test = part1(test_input)
    if p1_ans_test is not None:
        print("Part 1 (test):", p1_ans_test)
    p2_ans_test = part2(test_input)
    if p2_ans_test is not None:
        print("Part 2 (test):", p2_ans_test)

    # main part
    p1_ans = part1(puzzle_input)
    if p1_ans is not None:
        print("Part 1 (main):", p1_ans)
    p2_ans = part2(puzzle_input)
    if p2_ans is not None:
        print("Part 2 (main):", p2_ans)