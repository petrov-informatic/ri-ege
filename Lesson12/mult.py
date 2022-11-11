n = int(input())
mult = 1
for i in range(n):
    a = int(input())
    if 9 < a < 100:
    # if len(str(a)) == 2:
        mult *= a
print(mult)
