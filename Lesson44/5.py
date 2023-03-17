def f(x,y, m3, m5, p45):
    if x == y and m5 <= 4 and m3 >= 2 and p45 == 5:
        return 1
    if x >= y:
        return 0
    return f(x*5, y, m3, m5+1, p45) + f(x*3, y,m3+1, m5, p45) + f(x+45, y, m3, m5, p45+1)


print(f(1, 2970, 0, 0, 0))
