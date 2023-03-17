def add_two(x):
    return int(f'2{x}')


def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(add_two(x), y)


print(f(3, 678))
