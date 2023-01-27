def number(x):
    alf = 'abcde'
    if x > 9:
        x = alf[x-10]
    return int(f'123{x}5', 15) + int(f'1{x}233', 15)


for i in range(15):
    n = number(i)
    if n % 14 == 0:
        print(n // 14, i)
        break
