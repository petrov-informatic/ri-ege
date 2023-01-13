def alg(s):
    while '00' not in s:
        s = s.replace('01','210',1).replace('02','3101',1).replace('03','2012',1)
    return s


for ones in range(62):
    for twos in range(51):
        for threes in range(19):
            s = '0'+ones*'1'+twos*'2'+threes*'3'+'0'
            length = len(s)
            s = alg(s)
            if s.count('1')==61 and s.count('2')==50 and s.count('3') == 18:
                print(length)
