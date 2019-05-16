# Python 3.7
#
# CodeJam Solution by
# Curtis Babnik
# curtisbabnik@gmail.com

# This solution comes with some boilerplate that I use to speed along the process
#
# The intended use is to pipe input from a file. If you're not using a file for input
# then please send an EOF character with ctrl-Z in windows or ctrl-D in unix.

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
cl = 0  # current line index

raw_input = '\n'.join(lines)
tokens = []
for i in range(len(lines)):
    tokens.append(lines[i].split(' '))
ct = 0  # current token index

T = int(lines[0])  # number of tests/trials
cl += 1

for t in range(T):
    Nstr = lines[cl]
    N = int(Nstr)
    cl += 1
    # ====================
    # SOLUTION STARTS HERE
    # ====================

    a = b = ''
    for digit in Nstr:
        if digit == '0':
            a += '0'
            b += '0'
        elif digit == '5':
            a += '2'
            b += '3'
        else:
            a += str(int(digit) - 1)
            b += '1'
    a = int(a)
    b = int(b)
    if a == 0:
        a = b // 2 + b % 2
        b = b // 2

    result = '%d %d' % (a, b)
    print('Case #%d: %s' % ((t + 1), result))
