def f(x):
    return x**2 + 2*x + 1


a = [int(input()) for i in range(int(input()))]
# for i in a:
#     print(f(i))
b = [f(i) for i in a]
print(*a)
print(*b)

