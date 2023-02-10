a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = len(a)

count = 0
mx = float('-inf')
for i in range(n-1):
    for j in range(n):
        if (a[i]-a[j]) % 2 == 0 and a[i] * a[j] % 31 == 0:
            count += 1
            mx = max(mx, a[i]+a[j])
print(count, mx)
# 3138696 19982
