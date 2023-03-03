def f(x):
    if x > 200:
        return 1
    return f(x+1)


print(f(3))
