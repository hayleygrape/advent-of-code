import re

from utils.get_input import get_inputs, get_year_and_day
from utils.common import *

def move_box(b, row_num):
    row_str = "".join(b[row_num])
    can_push = re.search(r'(\@)(O+)(\.+)(.*)(#)', row_str)  # can push
    if can_push is not None:
        l,r = can_push.span(2)  # left, right locs of boxes in row
        b[row_num][l+1:r+1] = b[row_num][l:r]
        b[row_num][l] = '@'
        b[row_num][l-1] = '.'
    return b

def find_robot(b):
    for i in range(len(b)):
        m = re.search(r'@', "".join(b[i]))
        if m:
            return (i, m.span()[0])

def get_gps_cords(b):
    tot = 0
    for row,col in find_starts(b, 'O'):
        tot += (100*row)+col
    return tot

def part1(b):
    b, moves = clean(b)
    for move in moves:
        rots = {'<': 2, '^': 3, 'v': 1, '>': 0}
        rot_b = np.rot90(b, k=rots[move])
        row,col = find_robot(rot_b)
        if rot_b[row][col+1] == 'O':
            rot_b = move_box(rot_b, row)
        elif rot_b[row][col+1] == '.':
            rot_b[row][col+1] = '@'
            rot_b[row][col] = '.'
        b = np.rot90(rot_b, k=4-rots[move])
    return get_gps_cords(b)

def part2(b):
    pass

def clean(b):
    b,moves = b.split('\n\n')
    b = np.array([list(x) for x in b.split('\n')])
    moves = "".join(moves.split('\n'))
    return b,moves

if __name__=='__main__':
    puzzle_input, test_input = get_inputs(__file__, parse=False)

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