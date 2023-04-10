def time(data, id):
    process = [i for i in data if i[0]==str(id)][0]
    sub_ids = [int(i) for i in process[2].replace('"','').split('; ')]
    if process[2]=='0':
        return int(process[1])
    return int(process[1])+max([time(data, sub_id) for sub_id in sub_ids])


data = [i.split('\t') for i in open('1.txt').read().splitlines()[1:]]
print(max([time(data, int(process[0])) for process in data]))
