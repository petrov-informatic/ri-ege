def pr(x):
    p = 1
    while x > 0:
        p *= x % 10
        x //= 10
    return p


a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = len(a)
mx = max(a)
sums = []

for i in range(n-1):
    s = a[i]+a[i+1]
    if pr(s) != 0 and s % pr(s) == 0 and s < mx:
        sums.append(s)
print(len(sums), max(sums))
# 605 9612
