f = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(f)
even = [i for i in f if i % 2 == 0]
# even = []
# for i in f:
#     if i % 2 == 0:
#         even.append(i)
m = sum(even)/len(even)
mx = float('-inf')
count = 0
for i in range(n-1):
    if f[i] % 3 == 0 and f[i+1] < m or f[i] < m and f[i+1] % 3 == 0:
        count += 1
        mx = max(mx, f[i]+f[i+1])
print(count, mx)
