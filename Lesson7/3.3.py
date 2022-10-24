abc = int(input())
a = abc // 100
b = (abc // 10) % 10
c = abc % 10
if 2 * max(a, b, c) == a + b + c:
    print('Число интересное')
else:
    print('Число неинтересное')
