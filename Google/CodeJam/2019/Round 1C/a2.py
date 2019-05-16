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

# grab input
TF = input()
[T, F] = TF.split()
T = int(T)
F = int(F)  # unused

import sys
def debug(*args):
    print(*args, file=sys.stderr)

for t in range(T):
    # ====================
    # SOLUTION STARTS HERE
    # ====================

    solution = ''
    setrange = range(119)
    # i think this takes 148 checks
    for (offset, short) in [(0, 23), (1, 5), (2, 1), (3, 0), (4, 0)]:
        sets = {}
        sets['A'] = []
        sets['B'] = []
        sets['C'] = []
        sets['D'] = []
        sets['E'] = []
        for set in setrange:
            print(set*5+offset+1)
            figure = input()
            sets[figure].append(set)
        for c in 'ABCDE':
            if len(sets[c]) == short and c not in solution:
                solution += c
                setrange = sets[c]

    print(solution)
    response = input()
    if response == 'N':
        exit()
exit()
