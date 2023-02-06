a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = len(a)


def f(a1, b):
    return a1 % 9 == 0 and b % 8 == 3 and b % 9


maxes = []

for i in range(n-1):
    # if a[i] % 9 == 0 and a[i+1] % 8 == 3 and a[i+1] % 9 or a[i+1] % 9 == 0 and a[i] % 8 == 3 and a[i] % 9:
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        maxes.append(max(a[i], a[i+1]))
print(len(maxes), max(maxes))
# 252 9971
