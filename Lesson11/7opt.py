from time import time
n = int(input())
s = 0
t0 = time()
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        s += i
        s += n//i
if int(n**0.5)==n**0.5:
    s -= int(n**0.5)
t1 = time()
print(s, t1 - t0)