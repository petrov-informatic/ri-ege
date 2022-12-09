s = input()
m = (len(s) - 1) // 2
print(f'{s[m+1:]}{s[:m+1]}')
