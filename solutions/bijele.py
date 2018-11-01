# https://open.kattis.com/problems/bijele

from sys import stdin

proper_list = [1, 1, 2, 2, 2, 8]
output = ''

input_list = map(int,stdin.readline().rstrip("\n").split(' '))

for i in range(len(proper_list)):
    output += str(proper_list[i] - input_list[i]) + ' '

print output.rstrip(' ')
