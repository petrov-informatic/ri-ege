s = '1'+'8'*80
while '18' in s or '288' in s or '3888' in s:
    print(s)
    if '18' in s:
        s = s.replace('18', '2', 1)
    elif '288' in s:
        s = s.replace('288', '3')
    else:
        s = s.replace('3888', '1')
print(s)
