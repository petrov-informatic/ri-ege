a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = len(a)

maxes = []


def f(x):
    return x > 0 and len(str(x)) == 3 and x % 10 == 5


for i in range(n-2):
    if f(a[i+1]) and not f(a[i]) and not f(a[i+2]):
        maxes.append(sum(a[i:i+3]))
print(len(maxes), max(maxes))
# 18 14769
