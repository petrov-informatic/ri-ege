n = int(input())
flag = 1
for i in range(2, n):
    if n % i == 0:
        flag = 0
        break
if flag:
    print('Простое')
else:
    print('Составное')