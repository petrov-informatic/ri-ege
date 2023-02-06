from time import time
a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)

t1 = time()
pairs = []
for i in range(n):
    for j in range(i+1, n):
        if (a[i]+a[j]) % 2 and a[i] * a[j] % 3 == 0:
            pairs.append(a[i]+a[j])
print(len(pairs), max(pairs))

t2 = time()

groups = [[] for i in range(4)]
for i in a:
    if i % 3 == 0 and i % 2:
        groups[0].append(i)
    if i % 3 == 0 and i % 2 == 0:
        groups[1].append(i)
    if i % 3 and i % 2:
        groups[2].append(i)
    if i % 3 and i % 2 == 0:
        groups[3].append(i)
k = [len(i) for i in groups]
m = [max(i) if len(i) else float('-inf') for i in groups]
print(k[0]*(k[1]+k[3]) + k[1]*k[2], max(m[0]+m[1], m[0]+m[3], m[1]+m[2]))
t3 = time()
print(t2-t1, t3-t2)
