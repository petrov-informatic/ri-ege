def isprime(n):
    if n == 1:
        return None
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True


for i in range(1, 101):
    if isprime(i):
        print(i, end=' ')
