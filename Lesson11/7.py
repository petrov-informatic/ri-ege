from time import time
n = int(input())
s = 0
t0 = time()
for i in range(1, n+1):
    if n % i == 0:
        s = s + i
t1 = time()
print(s, t1-t0)
