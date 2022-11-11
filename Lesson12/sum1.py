n = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    a = int(input())
    if a % 2 == 0:
        sum1 += a
    else:
        sum2 += a
print(sum1, sum2)
