number = int(input())
if not 0 <= number <= 36:
    color = 'не существует'
elif number == 0:
    color = 'зелёный'
elif (((1 <= number <= 10 or 19 <= number <= 28) and number % 2 == 1)
    or ((11 <= number <= 18 or 29 <= number <= 36) and number % 2 == 0)):
    color = 'красный'
else:
    color = 'чёрный'
print(color)
