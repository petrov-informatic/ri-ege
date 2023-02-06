a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)

sums = []
for i in range(n-1):
    if a[i] % 7 == 0 and a[i+1] % 17 != 0 or a[i+1] % 7 == 0 and a[i] % 17 != 0:
        sums.append(a[i]+a[i+1])
print(len(sums), min(sums))
# 2510 -19677
