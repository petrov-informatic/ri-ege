for i in range(9999, 1000-1, -1):
    string = str(i)
    s1 = int(string[0])+int(string[1])
    s2 = int(string[3])+int(string[2])
    if s1 > s2:
        result = str(s2)+str(s1)
    else:
        result = str(s1)+str(s2)
    if result == '117':
        print(i)
        break
