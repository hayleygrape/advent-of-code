import re
from collections import Counter

from utils.get_input import get_inputs, get_year_and_day
from utils.common import *

def part1(b):
    for i in range(25):
        next_iter = []
        for stone in b:
            if stone == 0:
                next_iter.append(1)
            elif len(str(stone)) % 2 == 0:
                s_stone = str(stone)
                mid = (len(s_stone) // 2)
                n1, n2 = int(s_stone[:mid]), int(s_stone[mid:])
                next_iter += [n1, n2]
            else:
                next_iter.append(stone*2024)
        b = next_iter
    return len(next_iter)

def blink_once(num):
    res = []
    if num == 0:
        res.append(1)
    elif len(str(num)) % 2 == 0:
        s_stone = str(num)
        mid = len(s_stone) // 2
        n1, n2 = int(s_stone[:mid]), int(s_stone[mid:])
        res += [n1, n2]
    else:
        res.append(num*2024)
    return res

def part2(b):
    stones = Counter(b)
    count = 0
    for i in range(75):
        new_stones = Counter()
        for k,v in stones.items():
            res = blink_once(k)
            new_stones[res[0]] += v
            if len(res) == 2:
                new_stones[res[1]] += v
        stones = new_stones
    return sum(stones.values())

if __name__=='__main__':
    puzzle_input, test_input = get_inputs(__file__)
    puzzle_input = [int(x) for x in puzzle_input[0].split()]
    test_input = [int(x) for x in test_input[0].split()]

    # testing part
    print("\n===TESTING===")
    p1_ans_test = part1(test_input)
    if p1_ans_test is not None:
        print("Part 1:", p1_ans_test)
    p2_ans_test = part2(test_input)
    if p2_ans_test is not None:
        print("Part 2:", p2_ans_test)
    print("\n")

    # main part
    print("===MAIN===")
    p1_ans = part1(puzzle_input)
    if p1_ans is not None:
        print("Part 1:", p1_ans)
    p2_ans = part2(puzzle_input)
    if p2_ans is not None:
        print("Part 2:", p2_ans)
    print("\n")