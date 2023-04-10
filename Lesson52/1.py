def time(data, id):
    if data[id]['sub'][0] == 0:
        return data[id]['time']
    return data[id]['time'] + max([time(data, id_) for id_ in data[id]['sub']])


data = [i.split('\t') for i in open('1.txt').read().splitlines()[1:]]
data = {int(i[0]): {'time': int(i[1]), 'sub': [int(j) for j in i[2].replace('"', '').split('; ')]} for i in data}
print(max([time(data, id) for id in data]))

