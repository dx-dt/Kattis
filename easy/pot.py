# https://open.kattis.com/problems/pot

import sys

sum = 0
input = sys.stdin.read().split()
input.pop(0)

for entry in input:
    number = int(entry[:-1])
    exponent = int(entry[-1])
    sum += number**exponent

print sum
