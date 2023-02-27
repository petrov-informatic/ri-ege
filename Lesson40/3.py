def draw_triangle(fill, base):
    for i in range(base // 2 + 1):
        print(fill * (i+1))
    for i in range(base // 2, 0, -1):
        print(fill * i)


draw_triangle('+', 10)