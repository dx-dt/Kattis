# https://open.kattis.com/problems/conundrum

from sys import stdin

input = stdin.readline().rstrip("\n")

name = 'PER'
subs = 0

for i in range(len(input)/3):
    substring = (input[i*3:(i+1)*3])
    for j in range(len(substring)):
        if substring[j] != name[j]:
            subs +=1

print subs
