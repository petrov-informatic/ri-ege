n = int(input())
k = 0
while n > 0:
    if n % 10 == 4:
        k += 1
    n //= 10
print(k > 0)
# print('4' in input())
