def time(data, id):
    process = data[id]
    if process['sub'] == False:
        return process['time']
    return max([time(data, sub_id) for sub_id in process['sub']]) + 3 + process['time']


data = [i.split('\t') for i in open('3.txt').read().splitlines()[1:]]
data = {
    i[0]: {
        'time': int(i[1]),
        'sub': i[2].replace('"', '').split(';') if len(i) > 2 else False
    } for i in data
}
print(max([time(data, id) for id in data]))
