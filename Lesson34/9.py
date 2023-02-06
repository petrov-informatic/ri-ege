a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = len(a)
min103 = min([i for i in a if i % 103 == 0])

sums = []

for i in range(n-1):
    if (a[i]+a[i+1]) % 2 == 0 and (a[i] - a[i+1]) % min103 == 0:
        sums.append(a[i]+a[i+1])
print(len(sums), max(sums))
# 4 145300
