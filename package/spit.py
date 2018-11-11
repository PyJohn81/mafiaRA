def spitFunc():
    import json
    import random

    global seq
    seq = []

    with open('./gameData.txt' , 'r') as datafile:
        data = json.load(datafile)

    dictionary = data[1]

    for i in range(data[0]):
        seq.append(i)

    random.shuffle(seq)

    for i in seq:
        input(f'Your role is: {dictionary[str(i+1)]}\n')

if (__name__ == '__main__'):
    spitFunc()