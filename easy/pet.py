# https://open.kattis.com/problems/pet

import sys

n = 1
leader = None
highscore = 0

input = sys.stdin.read().split("\n")
input.pop()

for line in input:
    score = 0
    for value in line.split(' '):
        score += int(value)
    if score > highscore:
        leader = n
        highscore = score
    n += 1

print leader, highscore
