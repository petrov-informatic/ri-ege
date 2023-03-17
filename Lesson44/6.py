def f(x, y, count):
    if x == y and count % 2:
        return 1
    if x >= y:
        return 0
    return f(x+2, y, count + 1) + f(x * 2, y, count + 1) + (f(x**2, y, count + 1) if x > 1 else 0)


print(f(1, 100, 0))