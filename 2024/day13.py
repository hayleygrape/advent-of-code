import re
import decimal

from utils.get_input import get_inputs, get_year_and_day
from utils.common import *

def clean(b):
    in_x, in_y = [], []
    for value in b:
        info, nums = value.split(':')
        x,y = nums.split(',')
        if info.startswith('Button'):
            in_x.append(re.search(r'(X\+)(\d+)', x).groups()[1])
            in_y.append(re.search(r'(Y\+)(\d+)', y).groups()[1])
        elif info.startswith('Prize'):
            target_x = int(re.search(r'(X\=)(\d+)', x).groups()[1])
            target_y = int(re.search(r'(Y\=)(\d+)', y).groups()[1])
    in_x, in_y = [int(x) for x in in_x], [int(x) for x in in_y]
    return [in_x, in_y, [target_x, target_y]]

# 23188 too low
def part1(b):
    c = [clean(x) for x in b]
    total_cost = 0
    for in_x,in_y,targets in c:
        a = np.array([in_x, in_y])
        b = np.array(targets)
        x, y = np.round(np.linalg.solve(a, b), 10)
        if x % 1 == 0 and y % 1 == 0:
            total_cost += 3*x+y
    return total_cost

def part2(b):
    c = [clean(x) for x in b]
    to_add = '10000000000000'
    total_cost = 0
    for in_x,in_y,targets in c:
        targets = [int(to_add+str(t)) for t in targets]
        a = np.array([in_x, in_y])
        b = np.array(targets)
        x = np.round(np.linalg.solve(a, b), 0)
        # print((np.dot(a, x) == b))
        if (np.dot(a, x) == b).all():
            j = np.linalg.solve(a, b)
            print(in_x, in_y)
            print(decimal.Decimal.from_float(j[0]),decimal.Decimal.from_float(j[1]))
            print(decimal.Decimal.from_float(x[0]),decimal.Decimal.from_float(x[1]))
            print('\n')
            total_cost += (3*x[0])+x[1]  # test if correct bc numbers are stupid
    return total_cost

if __name__=='__main__':
    puzzle_input, test_input = get_inputs(__file__, parse=False)
    if len(puzzle_input)==1:
        puzzle_input = puzzle_input[0]
    if len(test_input)==1:
        test_input = test_input[0]
    
    puzzle_input, test_input = puzzle_input.split('\n\n'), test_input.split('\n\n')
    puzzle_input, test_input = [x.split('\n') for x in puzzle_input], [x.split('\n') for x in test_input]

    # testing part
    p1_ans_test = part1(test_input)
    if p1_ans_test is not None:
        print("Part 1 (test):", p1_ans_test)
    p2_ans_test = part2(test_input)
    if p2_ans_test is not None:
        print("Part 2 (test):", int(p2_ans_test))

    # main part
    p1_ans = part1(puzzle_input)
    if p1_ans is not None:
        print("Part 1 (main):", p1_ans)
    p2_ans = part2(puzzle_input)
    if p2_ans is not None:
        print("Part 2 (main):", int(p2_ans))

    # 4369768476874363904 too high
    # 4369768476874364000 too high
    # 2039632850434620928 too hgh