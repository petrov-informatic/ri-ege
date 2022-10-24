a, b, c = [float(i) for i in input().split()]
maxNumber = max(a, b, c)
minNumber = min(a, b, c)
print(maxNumber, a + b + c - maxNumber - minNumber, minNumber)
