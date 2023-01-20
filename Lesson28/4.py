# s = input().lower().split()
# print(f"Количество артиклей: {s.count('a')+s.count('an')+s.count('the')}")

print(f"Количество артиклей: {len([1 for i in input().lower().split() if i in ['a', 'an', 'the']])}")
