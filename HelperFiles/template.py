# Python 3.7
#
# Solution by
# Curtis Babnik
# curtisbabnik@gmail.com

# ==================
# Boiler Plate Setup
# ==================

# The following two libraries are installed on Google's test machines
#import numpy as np
#import scipy
# Standard libraries that may be useful
import sys
#import math
#import re
#import itertools

def read(lines=None):
    if lines is None:
        return input()
    ret = []
    for i in range(lines):
        ret[i] = input()
    return ret

def readTokens(lines=None):
    if lines is None:
        return input().split(' ')
    return list(map(lambda s:s.split(' '), read(lines)))

def readInts(lines=None):
    if lines is None:
        return list(map(int, readTokens()))
    return list(map(
        lambda line: list(map(int, line)),
        readTokens(lines)
    ))

def readFloats(lines=None):
    if lines is None:
        return list(map(float, readTokens()))
    return list(map(
        lambda line: list(map(float, line)),
        readTokens(lines)
    ))

# somewhat useful for the interactive problems
def printDebug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def interact(output):
    print(output)
    response = input()
    printDebug("%-20s%s" % (output, response))

def remote_debug():
    import time
    ready = False
    # manually attach to process and set this True
    while not ready:
        time.sleep(2)

T = readInts()[0]  # number of tests/trials
for t in range(T):
    # ====================
    # SOLUTION STARTS HERE
    # ====================

    result = 0
    print('Case #%d: %s' % ((t + 1), result))
