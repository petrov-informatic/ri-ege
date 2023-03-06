def is_prime(x):
    i = 2
    while i**2 <= x:
        if x % i == 0:
            return False
        i += 1
    return x != 1


for i in range(17*10**6, 23*10**6 - 1):
    if (2*i + 2) % 50000 == 0 and is_prime(i) and is_prime(i+2):
        print(i, i+2)
# 22049999 22050001
# 22424999 22425001
# 22574999 22575001
# 22949999 22950001
