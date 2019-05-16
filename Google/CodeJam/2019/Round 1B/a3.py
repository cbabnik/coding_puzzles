# Python 3.7
#
# Solution by
# Curtis Babnik
# curtisbabnik@gmail.com

# This solution comes with some boilerplate that I use to speed along the process
#
# The intended use is to pipe input from a file. If you're not using a file for input
# then please send an EOF character with ctrl-Z in windows or ctrl-D in unix.

from math import log2

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

def binarySearch(A, a, b, v, f=lambda x:x, d='unique'):
    if a >= b:
        if f(A[a]) == v:
            return a, True
        elif f(A[a]) > v:
            return a, False
        else:
            return a+1, False
    mp = (a+b)//2
    if f(A[mp]) == v:
        if d == 'unique':
            return mp, True
        elif d == 'left':
            return binarySearch(A, mp-1, b, v, f)
        elif d == 'right':
            return binarySearch(A, mp+1, b, v, f)
    elif f(A[mp]) <= v:
        return binarySearch(A, mp+1, b, v, f)
    else:
        return binarySearch(A, a, mp-1, v, f)

class RMQ_ST: # range minimum query sparse table
    def __init__(self, n, f):
        lgN = int(log2(n))
        self.f = f
        self.ST = []
        for i in range(n):
            self.ST.append([0] * (lgN+1))
            self.ST[i][0] = i
        for j in range(1, lgN+1):
            self.ST[n - 1][j] = n - 1
        for j in range(1, lgN+1):
            for i in range(n-1):
                self.ST[i][j] = min([self.ST[i][j - 1], self.ST[i + 1][j - 1]], key=f)

    def lookup(self, L, R):
        r = int(log2(R-L))
        return min([self.ST[L][r], self.ST[R-2**r][r]], key=self.f)

for t in range(T):
    # ====================
    # SOLUTION STARTS HERE
    # ====================
    N = int(tokens[cl][0])  # Swords
    K = int(tokens[cl][1])  # Fair threshold
    C = []
    D = []
    ct = 0
    for n in range(N):
        C.append(int(tokens[cl+1][ct]))
        D.append(int(tokens[cl+2][ct]))
        ct += 1
    cl += 3

    goods = 0

    STD = RMQ_ST(N, lambda x: -D[x])
    STC = RMQ_ST(N, lambda x: -C[x])

    for i in range(N):
        c = C[i]
        L1 = binarySearch(range(N), 0, i, c+K, lambda x: STD.lookup(x, i), 'left')[0]
        L2 = binarySearch(range(N), 0, i, c, lambda x: STC.lookup(x, i), 'left')[0]
        L = max(L1,L2)
        R1, found = binarySearch(range(N), 0, i, c+K, lambda x: STD.lookup(i, x), 'right')
        if not found:
            R1 -= 1
        R2, found = binarySearch(range(N), 0, i, c, lambda x: STC.lookup(i, x), 'right')
        if not found:
            R2 -= 1
        R = min(R1,R2)

        goods += 2**(R-L)

    result = goods
    print('Case #%d: %s' % ((t + 1), result))
