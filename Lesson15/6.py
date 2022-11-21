count = 0
for x in range(10, 100):
    if x % 7 == 3 and x % 2 == 1 and x % 5 == 2:
        count += 1
print(count)
