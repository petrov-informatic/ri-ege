a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = len(a)
numbers31 = [i for i in a if i % 31 == 0]
sums = []


def to5(x):
    number = ''
    while x:
        number = str(x % 5) + number
        x //= 5
    return number


for i in range(n-2):
    s = a[i]+a[i+1]+a[i+2]
    s5 = to5(s)
    if s5 == s5[::-1] and s / 3 > sum(numbers31) / len(numbers31):
        sums.append(s)
print(len(sums), min(sums))
# 206 16651
