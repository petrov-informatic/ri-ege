def f(x,y,A):
    return (( x<5 ) <= (x*x < A)) and ((y*y <= A) <= (y<=5))


count = 0
for A in range(1, 1000):
    flag = True
    for x in range(50):
        for y in range(50):
            if not f(x,y,A):
                flag = False
    if flag:
        count += 1
print(count)

