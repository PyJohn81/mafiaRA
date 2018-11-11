def keyInFunc():
    import json
    global data

    dictionary = {}
    num = int(input('Please key in the number of players:\n'))
    data = [num , dictionary]

    for i in range(1, num + 1):
        dictionary[i] = input(f'Please key in a role for player {i}:\n')
        print(dictionary)

    with open('gameData.txt' , 'w') as datafile:
        json.dump(data , datafile)

if (__name__ == '__main__'):
    keyInFunc()