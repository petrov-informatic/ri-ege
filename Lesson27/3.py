from string import ascii_lowercase as alf

# a = []
# for i in range(len(alf)):
#     a.append((i+1)*alf[i])
# print(a)

print([(i+1)*alf[i] for i in range(len(alf))])
