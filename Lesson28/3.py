# ip = [int(i) for i in input().split('.')]
# flag = 'ДА'
# for i in ip:
#     if i > 255 or i < 0:
#         flag = 'НЕТ'
#         break
# print(flag)
print('ДА' if len([int(i) for i in input().split('.') if int(i) in range(0, 256)]) == 4 else 'НЕТ')
