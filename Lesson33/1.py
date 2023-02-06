a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)

pairs = []
for i in range(n-1):
    if a[i] * a[i+1] % 3 == 0:
        pairs.append(a[i]+a[i+1])
print(len(pairs), max(pairs))
