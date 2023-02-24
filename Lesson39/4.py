def mask(a, b):
    return int(f'1{a}34567{b}9')


for i in range(10):
    for j in range(10):
        number = mask(i, j)
        if number % 17 == 0:
            print(number, number // 17)
