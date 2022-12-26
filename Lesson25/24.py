from random import shuffle

def alg(s):
    while '49' in s or '97' in s or '47' in s:
        if '47' in s:
            s = s.replace('47','74',1)
        if '97' in s:
            s = s.replace('97', '79', 1)
        if '49' in s:
            s = s.replace('49', '94', 1)
    return s


st = list(40*'9'+40*'7'+50*'4')
shuffle(st)
st1 = ''.join(st)
newStr = alg(st1)
print(st1)
print(newStr[24]+newStr[70]+newStr[104])
