def f(x, y, plus, mult):
    if x == y and mult > plus:
        return 1
    if x >= y:
        return 0
    return f(x+1, y, plus+1, mult) + f(x*2, y, plus, mult+1) + f(x*5, y, plus, mult+1)


print(f(3, 260, 0, 0))