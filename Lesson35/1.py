a = [int(i) for i in open(input()+'.txt').read().splitlines()]
# a = [8, (8**7-1)//7, 64, 100, 21]
n = len(a)

min21 = min([i for i in a if i % 21 == 0])


def sum8(x):
    x = oct(x)[2:]
    s = sum([int(i) for i in x])
    return s


sums = []
for i in range(n-1):
    if sum8(a[i]) == sum8(min21) or sum8(a[i+1]) == sum8(min21):
        sums.append(a[i]+a[i+1])
print(len(sums), min(sums))
# 1703 2281
