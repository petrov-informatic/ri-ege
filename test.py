n1 = int(input())
n2 = int(input())
n3 = int(input())
min1, min2, min3 = sorted([n1, n2, n3])
n = int(input())
while n != 0:
    if n < min1:
        min3 = min2
        min2 = min1
        min1 = n
    elif n < min2:
        min3 = min2
        min2 = n
    elif n < min3:
        min3 = n
    n = int(input())
print(min1, min2, min3)
