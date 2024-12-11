import re
import pdb

from utils.get_input import get_inputs, get_year_and_day
from utils.common import *

def part1(b):
    pass

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