for i in range(100, 1000):
    string = str(i)
    s1 = int(string[0])+int(string[1])
    s2 = int(string[1])+int(string[2])
    if str(s1)+str(s2) == '1412' or str(s1)+str(s2) == '1214':
        print(i)
        break
