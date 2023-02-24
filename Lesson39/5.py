def mask(a, b):
    return int(f'123{a}567{b}')


for star in list(range(100))+['']+[f'0{i}' for i in range(10)]:
    for que in range(10):
        number = mask(star, que)
        if number % 169 == 0:
            print(number, number // 169)
