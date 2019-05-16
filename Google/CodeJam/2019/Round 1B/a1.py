# Python 3.7
#
# Solution by
# Curtis Babnik
# curtisbabnik@gmail.com

# This solution comes with some boilerplate that I use to speed along the process
#
# The intended use is to pipe input from a file. If you're not using a file for input
# then please send an EOF character with ctrl-Z in windows or ctrl-D in unix.

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

for t in range(T):
    # ====================
    # SOLUTION STARTS HERE
    # ====================
    P = int(tokens[cl][0])
    Q = int(tokens[cl][1])
    cl += 1
    XYD = []
    for p in range(P):
        X = int(tokens[cl][0])
        Y = int(tokens[cl][1])
        D = tokens[cl][2]
        XYD.append((X,Y,D))
        cl += 1

    # we could do this with 20,000 ints, to represent the change of people going to each row and column
    X = [0]*Q
    Y = [0]*Q

    for xyd in XYD:
        (x,y,d) = xyd
        if d == 'N' and y != Q:
            Y[y+1] += 1
        elif d == 'S' and y != 0:
            Y[0] += 1
            Y[y] -= 1
        elif d == 'E' and x != Q:
            X[x+1] += 1
        elif d == 'W' and x != 0:
            X[0] += 1
            X[x] -= 1

    bestX = 0
    bestP = 0
    p = 0
    for x in range(len(X)):
        dp = X[x]
        p += dp
        if p > bestP:
            bestX = x
            bestP = p
    bestY = 0
    bestP = 0
    p = 0
    for y in range(len(Y)):
        dp = Y[y]
        p += dp
        if p > bestP:
            bestY = y
            bestP = p

    print('Case #%d: %s %s' % ((t + 1), bestX, bestY))
