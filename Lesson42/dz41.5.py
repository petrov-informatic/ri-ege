# import sys
# sys.setrecursionlimit(3600)


# print(7031*7029*7027)


# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (2 * n - 1) * f(n - 1)
#
#
# print(f(3516))


d = [1 for i in range(3517)]
for i in range(2, 3517):
    d[i] = (2 * i - 1) * d[i-1]
print(d[3516]/d[3513])
