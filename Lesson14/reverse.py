n = int(input())
b = ''
while n > 0:
    a = n % 10
    b += str(a)
    n //= 10
print(b)