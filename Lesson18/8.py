s = input()
# print(f'@ - {s.count("@")}, * - {s.count("*")}')
dogs = 0
stars = 0
for n in s:
    if n == '@':
        dogs += 1
    if n == '*':
        stars += 1
print(f'@ - {dogs}, * - {stars}')
