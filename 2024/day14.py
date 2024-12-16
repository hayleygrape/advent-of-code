import re
from collections import Counter
import math

from utils.get_input import get_inputs, get_year_and_day
from utils.common import *

def print_state(row,col,c):
    to_print = ''
    for i in range(row):
        for j in range(col):
            if (i,j) in c:
                to_print += str(c[(i,j)])
            else:
                to_print += '.'
        to_print += '\n'
    print(to_print)

def part1(b):
    c = Counter()
    max_row, max_col = 101, 103
    # max_row, max_col = 7,11
    for robot in b:
        start, slope = robot.split(' ')
        start = start.lstrip('p=')
        slope = slope.lstrip('v=')
        col,row = [int(x) for x in start.split(',')]
        run, rise = [int(x) for x in slope.split(',')]
        pos = (row,col)
        for i in range(100):
            pos = (pos[0] + rise, pos[1] + run)
        final_pos = (pos[0] % max_row, pos[1] % max_col)
        c[final_pos] += 1
    mid_row, mid_col = max_row//2, max_col//2
    print_state(max_row, max_col, c)
    up_right, up_left, down_right, down_left = 0,0,0,0
    for row,col in c:
        if row < mid_row and col < mid_col:
            up_left += c[(row,col)]
        elif row < mid_row and col > mid_col:
            up_right += c[(row,col)]
        elif row > mid_row and col < mid_col:
            down_left += c[(row,col)]
        elif row > mid_row and col > mid_col:
            down_right += c[(row,col)]

    print(up_right, up_left, down_right, down_left)
    return math.prod([up_right, up_left, down_right, down_left])

def part2(b):
    pass

if __name__=='__main__':
    puzzle_input, test_input = get_inputs(__file__)
    if len(puzzle_input)==1:
        puzzle_input = puzzle_input[0]
    if len(test_input)==1:
        test_input = test_input[0]

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

    # 213532410 -- too low