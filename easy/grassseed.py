# https://open.kattis.com/problems/grassseed

from sys import stdin

sum = 0.0

input = stdin.read().split('\n')
input.pop()
cost = float(input.pop(0))
input.pop(0)

for line in input:
    l,w = map(float,line.split(' '))
    sum += l*w*cost

print sum
