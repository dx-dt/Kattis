# https://open.kattis.com/problems/qaly

from sys import stdin

sum = 0.0
for line in stdin.readlines():
    if len(line) <= 4:
        continue
    q,l = map(float,line.split(' '))
    sum += q*l
print sum
