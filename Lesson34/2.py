a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)

count = 0
mn = float('inf')

for i in range(n-1):
    if a[i+1] > a[i]:
        count += 1
        mn = min(mn, abs(a[i+1]-a[i]))
print(count, mn)
# 2521 5
