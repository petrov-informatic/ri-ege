n = int(input())
s = 0
for i in range(1, n+1):
    last = i**2 % 10
    if last == 2 or last == 5 or last == 8:
        s = s + i
print(s)
