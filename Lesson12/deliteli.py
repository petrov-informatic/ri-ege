n = int(input())
s = 0
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        s += i
        s += n // i
if int(n**0.5) == n**0.5:
    s -= int(n**0.5)
print(s)