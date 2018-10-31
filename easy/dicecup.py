# https://open.kattis.com/problems/dicecup

from sys import stdin

m,n = map(int,stdin.readline().rstrip("\n").split(' '))

possibilites = {}
result = {'outcomes': [], 'value': 0}

for i in range(1,m+1):
    for j in range(1,n+1):
        try:
            possibilites[i+j] += 1
        except KeyError:
            possibilites[i+j] = 1

for key in possibilites.keys():
    if possibilites[key] > result['value']:
        result['outcomes'] = [key]
        result['value'] = possibilites[key]
    elif possibilites[key] == result['value']:
        result['outcomes'].append(key)

for outcome in result['outcomes']:
    print outcome
