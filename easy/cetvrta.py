# https://open.kattis.com/problems/cetvrta

from sys import stdin

coordinates = [[],[]]
output = ''

for row in stdin.read().rstrip("\n").split("\n"):
    for axis, value in enumerate(row.split(' ')):
        coordinates[axis].append(value)

for axis in coordinates:
    for value in axis:
        if axis.count(value) == 1:
            output += value + ' '

print output.rstrip(' ')
