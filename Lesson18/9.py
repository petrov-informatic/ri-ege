n = int(input())
number = ''
while n > 0:
    x = n % 2
    n //= 2
    number = str(x) + number
print(number)
