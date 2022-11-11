a, b = int(input()), int(input())
count = 0
for i in range(a, b+1):
    if i**2 % 10 == 6 and i % 10 != 4:
        count = count + 1
print(count)
