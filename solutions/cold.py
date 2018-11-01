# https://open.kattis.com/problems/cold

from sys import stdin

n = 0

stdin.readline()

for temp in map(int,stdin.readline().rstrip("\n").split(' ')):

    if temp < 0:
        n += 1

print n
