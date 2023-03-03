def F(n):
    if n == 0:
        return 0
    elif n > 0 and n % 3 == 2:
        return F(n-1)+1
    return F((n - (n % 3)) // 3)


n = 0
while True:
    if F(n) == 5:
        print(n)
        break
    n += 1
# 242
