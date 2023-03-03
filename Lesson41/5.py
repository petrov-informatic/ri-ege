import sys

sys.setrecursionlimit(2050)


def F(n):
    # d = [1 for i in range(n+1)]
    # for i in range(2, n+1):
    #     d[i] = d[i-1] * i
    # return d[n]
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)


print(F(2023) / F(2020))
