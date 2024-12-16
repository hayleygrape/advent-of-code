import re
from itertools import chain
from collections import deque

from utils.get_input import get_inputs, get_year_and_day
from utils.common import *

def find_contiguous(b):
    all_visited = {(0,0)}
    contig_map = {}
    for i in range(len(b)):
        for j in range(len(b[i])):
            if (i,j) in all_visited:
                continue
            visited = {(i,j)}
            q = deque([(i,j)])
            start_val = b[i][j]
            count = 0
            while len(q) > 0:
                loc = q.popleft()
                n = get_immediate_neighbors(loc[0], loc[1])
                if count > 20:
                    break
                for row,col in n:
                    if check_bounds(b,row,col) and b[row][col] == start_val and (row,col) not in visited:
                        q.append((row,col))
                        visited.add((row,col))
                        all_visited.add((row,col))
            if start_val not in contig_map:
                contig_map[start_val] = []
            contig_map[start_val].append(visited)
    return contig_map

def get_area(plots, plant_type):
    plots = "".join(plots)
    area = re.findall(rf'{plant_type}', plots, re.MULTILINE)
    return len(area)

def get_perimeter(plant_area_locs):
    num_adj = {i:0 for i in range(0, 5)}
    for row,col in plant_area_locs:
        neighbors = get_immediate_neighbors(row, col)
        amt = len(set(neighbors).intersection(plant_area_locs))  # num touching other plots of the same type
        num_adj[4-amt] += 1
    return sum(k*v for k,v in num_adj.items())

def part1(b):
    contig_map = find_contiguous(b)
    area = {k:[len(x) for x in contig_map[k]] for k in contig_map}
    perim = {k: [get_perimeter(x) for x in contig_map[k]] for k in contig_map}
    total = 0
    for k,v in area.items():
        for i in range(len(v)):
            total += area[k][i]*perim[k][i]
    return total

def part2(b):
    pass

if __name__=='__main__':
    puzzle_input, test_input = get_inputs(__file__)
    run_main = True

    # testing part
    p1_ans_test = part1(test_input)
    if p1_ans_test is not None:
        print("Part 1 (test):", p1_ans_test)
    p2_ans_test = part2(test_input)
    if p2_ans_test is not None:
        print("Part 2 (test):", p2_ans_test)

    if run_main:
        # main part
        p1_ans = part1(puzzle_input)
        if p1_ans is not None:
            print("Part 1 (main):", p1_ans)
        p2_ans = part2(puzzle_input)
        if p2_ans is not None:
            print("Part 2 (main):", p2_ans)