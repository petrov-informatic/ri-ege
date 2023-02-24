def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


numbers = []
# number = 0
for i in range(1547341, 1547409+1):
    if is_prime(i):
        numbers.append(i)
        # number += 1
        # print(number, i)
print(*[f'{i+1} {numbers[i]}' for i in range(len(numbers))], sep='\n')
