def unique(x):
    x = str(x)
    return int(x[2]) % 2 == 0 and int(x[4]) % 2 == 0


numbers = []
for i in range(33333, 55555+1):
    if i % 6 and i % 7 and i % 8 and unique(i):
        numbers.append(i)
print(len(numbers), max(numbers)-min(numbers))
