# Python 3.7
#
# Solution by
# Curtis Babnik
# curtisbabnik@gmail.com

TW = input()
[T, W] = TW.split()
T = int(T)
W = int(W)  # unused

for t in range(T):
    # number that keeps R6 and R5 within 2**7 factor difference and doesn't cut out R4
    # N//6 - N//5 >= 7
    # N//4 <= 55
    # N == 220 satisfies
    print(220)
    valA = int(input())
    # number that keeps R3 and R2 within 2**7 factor difference and doesn't cut out R1
    # N//3 - N//2 >= 7
    # N//1 <= 55
    # N == 55 satisfies
    print(55)
    valB = int(input())

    r6a = valA % 2 ** (220 // 5)
    r5a = valA % 2 ** (220 // 4) - r6a
    r4a = valA - r6a - r5a
    r6 = r6a // 2 ** (220 // 6)
    r5 = r5a // 2 ** (220 // 5)
    r4 = r4a // 2 ** (220 // 4)

    r6b = r6 * 2 ** (55 // 6)
    r5b = r5 * 2 ** (55 // 5)
    r4b = r4 * 2 ** (55 // 4)
    valB -= r6b + r5b + r4b
    r3b = valB % 2 ** (55 // 2)
    r2b = valB % 2 ** (55 // 1) - r3b
    r1b = valB - r3b - r2b
    r3 = r3b // 2 ** (55 // 3)
    r2 = r2b // 2 ** (55 // 2)
    r1 = r1b // 2 ** (55 // 1)

    print('%s %s %s %s %s %s' % (r1, r2, r3, r4, r5, r6))
    result = int(input())
    if result < 0:
        exit()
exit()
