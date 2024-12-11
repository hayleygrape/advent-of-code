import re

from utils.get_input import get_inputs, get_year_and_day
from utils.common import *

def get_next(pos,num,board):
    next_pos = set()
    for row,col in get_neighbors(pos[0], pos[1]):
        if board[row][col] != "." and int(board[row][col]) == num:
            next_pos.add((row,col))
    return next_pos

def part1(b):
    b = pad_input(b, fill='.')
    start_list = []
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] != "." and int(f[i][j]) == 0:
                start_list.append((i,j))
    paths = 0
    for cord in start_list:
        curr_locs = [cord]
        for i in range(1, 10):
            next_locs = [] # change to list for part 2
            for pos in curr_locs:
                next_locs += list(get_next(pos, i, f))
            curr_locs = next_locs
        paths += len(next_locs)

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