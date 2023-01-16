from string import ascii_lowercase as alf

a = [1,2,3,4]
print('\n'.join([str(i) for i in a]))
print(*a, sep='\n')
