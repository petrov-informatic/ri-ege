a, b, c = [int(i) for i in input().split()]
if c < b < a or a < b < c:
    answer = b
elif b < c < a or a < c < b:
    answer = c
else:
    answer = a
print(answer)
answer = a+b+c - min(a, b, c) - max(a, b, c)
print(answer)

