from math import ceil
a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = len(a)


# def full(i1, n1):
#     return abs(i1**(1/n1) - ceil(i1**(1/n1))) < 0.0001
# def full(i1, n1):
#     e = ceil(i1**(1/n1))
#     for j in range(n1):
#         i1 //= e
#     if i1 == 1:
#         return True
#     return False
# def full(i1, n1):
#     temp = int(i1**(1/n1))
#     for j in range(temp,temp+2):
#         if j**n1 == i1:
#             return True
#     return False

sqrs = []
cubes = []
k = 0
while k**2 <= 30000:
    sqrs.append(k**2)
    cubes.append(k**3)
    k += 1


def full(i1, n1):
    return (i1 in sqrs) if n1 == 2 else (i1 in cubes)


# while 1: print(full(int(input()),3))
M = max([i for i in a if full(i, 3)])
# p_pr = []
# p_sum = []
p = []
for i in range(n-2):
    three = a[i:i+3]
    d = abs(M - sum(three))
    if full(d, 2) and d % 2 == 0:
        t = sorted(three)
        p.append([t[0]*t[1], sum(t)])
        # p_pr.append(t[0]*t[1])
        # p_sum.append(sum(t))
# print(len(p_pr), p_pr[p_sum.index(max(p_sum))])
def key(element):
    return element[1]
p.sort(key=key)
print(len(p), p[-1][0])
# 15 30033000
