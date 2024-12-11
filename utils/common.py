import pandas as pd
import numpy as np
import networkx as nx
from itertools import combinations

def pad_input(b, fill="."):
    b = [fill*len(b)] + f + [fill*len(b)]
    b = [fill + x + fill for x in b]

def find_starts(b, str_to_find, limit=None, regex=False):
    # write later
    pass

# GETTING NEIGHBORS
def get_immediate_neighbors(row, col, include_self=False):
    """Get only up, down, left, right neighbors"""
    n = [(row-1, col), (row, col-1), (row, col+1), (row+1, col)]
    return n+[(row,col)] if include_self else n

def get_diag_neighbors(row, col, include_self=False):
    """Get neighbors including diagonal"""
    top_row = [(row-1, col) for col in range(col-1, col+1)]
    bottom_row = [(row+1, col) for col in range(col-1, col+1)]
    middle = [(row,col-1), (row,col+1)]
    n = top_row + bottom_row + middle
    return n+[(row,col)] if include_self else n

def get_shape(m, n, include_self=False):
    # write later
    pass