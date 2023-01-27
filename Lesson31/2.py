def cc(n, base):
    a = []
    while n:
        a.append(n % base)
        n //= base
    return a[::-1]


a = cc(7*512**1912+6*64**1954+5*8**1991-4*8**1980-2022,8)
print(a.count(7))

print(oct(7*512**1912+6*64**1954+5*8**1991-4*8**1980-2022)[2:].count('7'))

a = 7*512**1912+6*64**1954+5*8**1991-4*8**1980-2022
count = 0
while a != 0:
    if a % 8 == 7:
        count += 1
    a //= 8
print(count)
