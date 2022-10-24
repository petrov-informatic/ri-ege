score = int(input())
if score >= 90:
    mark = 5
else:
    if score >= 80:
        mark = 4
    else:
        if score >= 70:
            mark = 3
        else:
            if score >= 60:
                mark = 2
            else:
                mark = 1
print(mark)
