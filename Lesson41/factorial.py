from time import time


def fact(x):
    if x > 0:
        return fact(x-1) * x
    return 1


n = int(input())
t0 = time()
print(fact(n), fact(n-1))
t1 = time()
d = [1 for i in range(n+1)]
for i in range(1, n+1):
    d[i] = d[i-1] * i
print(d[n], d[n-1])
t2 = time()
print(t1-t0, t2-t1)
