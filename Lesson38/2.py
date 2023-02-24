def is_prime(x):
    i = 2
    while i**2 <= x:
        if x % i == 0:
            return False
        i += 1
    return True


number = 0
for i in range(2532000, 2532160+1):
    if is_prime(i) and i % 10 == 7:
        number += 1
        print(number, i)
