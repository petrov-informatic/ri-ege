month = int(input())
if month == 2:
    days = 28
elif (month < 8 and month % 2 == 1) or (month > 7 and month % 2 == 0):
    days = 31
else:
    days = 30
print(days)
