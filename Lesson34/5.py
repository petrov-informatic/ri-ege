a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = len(a)

numbers = []

for i in a:
    if i > 100 and (i // 10) % 10 <= 4 and (i // 100) % 10 in range(3, 8):
        numbers.append(i)
print(len(numbers), min(numbers))
# 502 1305
