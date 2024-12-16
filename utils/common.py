import pandas as pd
import numpy as np
import networkx as nx
from itertools import combinations

def pad_input(b, fill="."):
    b = [fill*len(b)] + b + [fill*len(b)]
    b = [fill + x + fill for x in b]
    return b

def find_starts(b, strs_to_find, limit=None, regex=False):
    # write later
    found = 0
    locs = []
    for i in range(len(b)):
        for j in range(len(b[i])):
            if regex:
                if re.fullmatch(regex, s) is not None:
                    locs.append((i,j))
                    found += 1
                    if limit is not None and found == limit:
                        return locs
            elif b[i][j] in strs_to_find:
                locs.append((i,j))
                found += 1
                if limit is not None and found == limit:
                    return locs
    return locs

# HELPERS
def check_bounds(b, row, col):
    if row >= 0 and row < len(b) and col >= 0 and col < len(b[0]):
        return True
    else:
        return False 

# GETTING NEIGHBORS
def get_immediate_neighbors(row, col, include_self=False):
    """Get only up, down, left, right neighbors"""
    n = [(row-1, col), (row, col-1), (row, col+1), (row+1, col)]  # order = up, left, right, down
    return n+[(row,col)] if include_self else n

def get_diag_neighbors(row, col, include_self=False):
    """Get neighbors including diagonal"""
    top_row = [(row-1, col) for col in range(col-1, col+2)]
    bottom_row = [(row+1, col) for col in range(col-1, col+2)]
    middle = [(row,col-1), (row,col+1)]
    n = top_row + bottom_row + middle
    return n+[(row,col)] if include_self else n

def get_shape(m, n, include_self=False):
    # write later
    pass