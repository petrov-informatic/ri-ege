from math import sqrt

a = float(input())
b = float(input())
arithmetic = (a + b) / 2
geometric = sqrt(a * b)
harmonic = 2 * a * b / (a + b)
square = sqrt((a**2+b**2)/2)
print(arithmetic, geometric, harmonic, square)
