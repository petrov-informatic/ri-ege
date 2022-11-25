n = int(input())
flag = 0
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        flag = 1
        print(i)
        break
if not flag:
    print(n)

