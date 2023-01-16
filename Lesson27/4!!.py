def d(n):
    a = []
    b = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            a.append(i)
            b.append(n // i)
        if i**2 == n:
            a.pop()
    return a+b[::-1]


print(d(1636466464))