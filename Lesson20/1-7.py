s = input()
answers1 = [
    len(s),
    s*3,
    s[0],
    s[:3],
    s[-3:],
    s[::-1],
    s[1:-1]
]
answers2 = [
    s[2],
    s[-2],
    s[:5],
    s[:-2],
    s[::2],
    s[1::2],
    s[-1::-2]
]
for i, answer in enumerate(answers1):
    print(f'{i + 1}. {answer}')
print()
for i in range(len(answers2)):
    print(f'{i+1}. {answers2[i]}')
