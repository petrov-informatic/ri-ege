a = int(input())
s = ''
while a % 9 == 0:
    s += str(a)+', '
    a = int(input())
print(s+str(a))

