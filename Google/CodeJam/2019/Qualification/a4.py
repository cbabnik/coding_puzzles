# Python 3.7
#
# Solution by
# Curtis Babnik
# curtisbabnik@gmail.com

# This solution comes with some boilerplate that I use to speed along the process
#
# The intended use is to pipe input from a file. If you're not using a file for input
# then please send an EOF character with ctrl-Z in windows or ctrl-D in unix.


T = int(input())
for t in range(T):
    # SOLUTION STARTS HERE
    # --------------------
    NBF = input().split(' ')
    N = int(NBF[0])
    B = int(NBF[1])  # at most 15
    F = int(NBF[2])
    # make F calls to test, then declare which of the B workers are broken

    # I imagine test set 2 is difficult, but test set 1 seems ok, I'll start with it.
    # my strategy is to just do like a binary sort

    # for test set 2 it may be worth noting that 15 in binary is 11111, 5 digits

    TEST_BITS = []
    for i in range(10):
        runlen = 2 ** (9 - i)
        runs = 2 ** i
        TEST_BITS.append(('0' * runlen + '1' * runlen) * runs)

    for i in range(10):
        print(TEST_BITS[i][:7])
        RETURN = input() + TEST_BITS[i][7:]

    result = 0
    print('Case #%d: %s' % ((t + 1), result))
    input()
