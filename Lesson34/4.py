a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)


def f(x):
    return len([1 for j in a[i:i+3] if j % x == 0])


avgs = []
for i in range(n-2):
    if f(3) == 3 and f(12) > 0:
        avgs.append(sum(a[i:i+3])/3)
print(len(avgs), min(avgs))
# 119 -7213.0
