k = 0
solutions = ''
for x in range(1, 777):
    for y in range(1, 777):
        if 12*x+13*y == 777:
            solutions += f'({x}, {y})\n'
            k += 1
print(k, solutions, sep='\n')

