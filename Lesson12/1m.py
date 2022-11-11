a, b = int(input()), int(input())
count = 0
for i in range(a, b+1):
    if i % 10 == 6:
        count = count + 1
print(count)
