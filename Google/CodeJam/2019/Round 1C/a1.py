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
    A = ints[cl][0]
    cl += 1

    C = []
    for i in range(A):
        C.append(lines[cl])
        cl += 1

    solution = ''
    while True:
        hasR = False
        hasP = False
        hasS = False
        for i in range(A):
            if C[i] == '':
                continue
            if C[i][0] == 'R':
                hasR = True
            elif C[i][0] == 'P':
                hasP = True
            elif C[i][0] == 'S':
                hasS = True
            C[i] = C[i][1:] + C[i][0]
        if hasR and hasP and hasS:
            solution = 'IMPOSSIBLE'
            break
        elif len(solution) == 500:
            # everything else must be subset which expands to be equal to my program, check if it becomes inequal
            # if inequal, whos loss is it?
            for i in range(A):
                if C[i] != '':
                    if 500 % len(C[i]) == 0:
                        solution = 'IMPOSSIBLE'
                        break
                    else:
                        # eventually someone loses

            solution = 'IMPOSSIBLE'
            break
        elif hasR and hasP:
            solution += 'P'
            for i in range(A):
                if C[i] != '':
                    if C[i][-1] == 'R':
                        C[i] = ''
        elif hasR and hasS:
            solution += 'R'
            for i in range(A):
                if C[i] != '':
                    if C[i][-1] == 'S':
                        C[i] = ''
        elif hasP and hasS:
            solution += 'S'
            for i in range(A):
                if C[i] != '':
                    if C[i][-1] == 'P':
                        C[i] = ''
        elif hasR:
            solution += 'P'
            break
        elif hasP:
            solution += 'S'
            break
        elif hasS:
            solution += 'R'
            break
        else:
            break

        # the latest something may be defeated though is at 500*500, and the program could be any of my first 500
        # if i can do 500^3 thats ok, 500^4 is not ok
        # so i need to find where to cut off my repeating pattern in constant time, maybe by finding the largest unique repeating amount
        # but i dont have to... ahh

    print('Case #%d: %s' % ((t + 1), solution))
