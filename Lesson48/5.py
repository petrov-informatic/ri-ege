def f(x,y,A):
    return y+2*x != 48 or x>A or y > x

for A in range(100,-1,-1):
    flag = True
    for x in range(500):
        for y in range(500):
            if not f(x,y,A):
                flag = False
    if flag:
        print(A)
        break