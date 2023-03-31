def f(x,y,A):
    return (( x<=9 ) <= (x*x <= A)) and ((y*y <= A) <= (y<=9))


for A in range(1000, 0, -1):
    flag = True
    for x in range(1, 50):
        for y in range(1, 50):
            if not f(x,y,A):
                flag = False
    if flag:
        print(A)
        break

