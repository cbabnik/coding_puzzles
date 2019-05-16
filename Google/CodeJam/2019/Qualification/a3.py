# Python 3.7
#
# Solution by
# Curtis Babnik
# curtisbabnik@gmail.com

# This solution comes with some boilerplate that I use to speed along the process
#
# The intended use is to pipe input from a file. If you're not using a file for input
# then please send an EOF character with ctrl-Z in windows or ctrl-D in unix.

from math import gcd, log2, floor

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
ct = 0  # current token index

T = int(lines[0])  # number of tests/trials
cl += 1

def accurate_divide(dividend, divisor):
    # this algorithm assumes that the two values divide perfectly
    r = 0
    power = floor(log2(dividend))
    while power >= 0:
        prod = divisor * 2**power
        if prod <= dividend:
            dividend -= prod
            r += 2**power
        power -= 1
    return r

for t in range(T):
    # SOLUTION STARTS HERE
    # --------------------

    # I'll be trying by using greatest common denominator to find the primes

    N = int(tokens[cl][0])
    L = int(tokens[cl][1])

    ENCODED = []
    for l in range(L):
        ENCODED.append(int(tokens[cl + 1][l]))
    PRIMES = [0]*(len(ENCODED)+1)
    DECODED = ''

    i = 1
    while ENCODED[i] == ENCODED[i - 1]:
        i += 1
    PRIMES[i] = gcd(ENCODED[i], ENCODED[i - 1])  # the prime is the only common divisor (other than 1)
    j = i - 1
    while j >= 0:
        PRIMES[j] = accurate_divide(ENCODED[j],PRIMES[j+1])
        j -= 1
    j = i + 1
    while j <= L:
        PRIMES[j] = accurate_divide(ENCODED[j-1],PRIMES[j-1])
        j += 1

    # now encoded is just the primes
    A = set(PRIMES)
    A = sorted(list(A))
    B = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for x in PRIMES:
        idx = A.index(x)
        DECODED += B[idx]

    result = DECODED
    print('Case #%d: %s' % ((t + 1), result))
    cl += 2
