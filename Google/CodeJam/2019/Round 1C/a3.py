# Python 3.7
#
# Solution by
# Curtis Babnik
# curtisbabnik@gmail.com

# This solution comes with some boilerplate that I use to speed along the process
#
# The intended use is to pipe input from a file. If you're not using a file for input
# then please send an EOF character with ctrl-Z in windows or ctrl-D in unix.

# The following two libraries are installed on Google's test machines
#import numpy as np
#import scipy
# Standard libraries that may be useful
#import math
#import re
#import itertools
from copy import deepcopy

# grab input
lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
cl = 0  # current line index

# put input into different shapes
raw_input = '\n'.join(lines)
tokens = []
for i in range(len(lines)):
    tokens.append(lines[i].split(' '))
def tryInt(s):
    try: return int(s)
    except ValueError: return None
def tryFloat(s):
    try: return int(s)
    except ValueError: return None
ints = list(map(lambda arr: list(map(tryInt,arr)), tokens))
floats = list(map(lambda arr: list(map(tryFloat,arr)), tokens))
ct = 0  # current token index

T = int(lines[0])  # number of tests/trials
cl += 1

for t in range(T):
    # ====================
    # SOLUTION STARTS HERE
    # ====================
    R, C = ints[cl]
    cl += 1

    G = []
    for r in range(R):
        G.append(lines[cl])
        cl += 1

    # section solving, cut a line each time, max 8! breakdowns. very very managable
    def solve(GG):
        GR = len(GG)
        if GR == 0:
            return 0
        GC = len(GG[0])
        if GC == 0:
            return 0
        for r in range(GR):
            row = map(lambda c: GG[r][c], range(GC))
            if '#' not in row:
                sols +=

    sols = 0
    # small set first, R,C <= 4

    result = sols
    print('Case #%d: %s' % ((t + 1), result))
