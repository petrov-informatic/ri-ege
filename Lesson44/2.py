def f(x, y, count):
    if x == y and count <= 4:
        return 1
    if x >= y:
        return 0
    return f(x+2, y, count + 1 if (x+2)%6==0 else count) + f(x*2, y, count+1 if (x*2)%6==0 else count) + f(x*3, y, count+1 if (x*3)%6==0 else count)


print(f(1, 300, 0))
