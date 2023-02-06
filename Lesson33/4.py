f = [int(i) for i in open(f'{input()}.txt').read().splitlines()]

max_sqr = max([i for i in f if abs(i) % 10 == 3])**2

count = 0
mx = float('-inf')
for i in range(len(f)-1):
    if int(abs(f[i]) % 10 == 3) ^ int(abs(f[i+1]) % 10 == 3):
        sum_sqr = f[i] ** 2 + f[i+1] ** 2
        if sum_sqr >= max_sqr:
            count += 1
            mx = max(mx, sum_sqr)
print(count, mx)
