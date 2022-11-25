n = int(input())
table = ''
for i in range(1, n + 1):
    for j in range(1, 10):
        table += f'{i} + {j} = {i+j}\n'
print(table)
