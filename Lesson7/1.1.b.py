score = int(input())
if score > 100:
    mark = 'Error'
elif score >= 90:
    mark = 5
elif score >= 80:
    mark = 4
elif score >= 70:
    mark = 3
elif score >= 60:
    mark = 2
else:
    mark = 1
print(mark)
