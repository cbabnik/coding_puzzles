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
    # SOLUTION STARTS HERE
    # --------------------
    # I think i can just take the transpose of her maze?
    N = int(lines[cl])
    P = lines[cl + 1]
    cl += 2

    table = str.maketrans('SE', 'ES')
    P = P.translate(table)

    result = P
    print('Case #%d: %s' % ((t + 1), result))
