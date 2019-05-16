from math import log2

# THIS ONE NOT FINISHED
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


if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    print(binarySearch(arr, 0, 5, 0.5), (0, False))
    print(binarySearch(arr, 0, 5, 1), (0, True))
    print(binarySearch(arr, 0, 5, 1.5), (1, False))
    print(binarySearch(arr, 0, 5, 2), (1, True))
    print(binarySearch(arr, 0, 5, 3.5), (3, False))
    print(binarySearch(arr, 0, 5, 6), (5, True))
    print(binarySearch(arr, 0, 5, 7), (6, False))

    arr = [2, 4, 3, 1, 6, 7, 8, 9, 1, 7]
    st = RMQ_ST(len(arr), lambda idx: arr[idx])
    print(st.lookup(0, 1), 0)
    print(st.lookup(1, 2), 1)
    print(st.lookup(2, 3), 2)
    print(st.lookup(0, 5), 3)
    print(st.lookup(1, 6), 3)
    print(st.lookup(2, 7), 3)
    print(st.lookup(2, 8), 3)
    print(st.lookup(2, 9), 3)
    print(st.lookup(0, 10), 3)
