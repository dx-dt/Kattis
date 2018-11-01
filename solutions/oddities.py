# https://open.kattis.com/problems/oddities

import sys

input = sys.stdin.read().split()
input.pop(0)

for number in input:
    if int(number) % 2 == 0:
        oddity = 'even'
    else:
        oddity = 'odd'
    print "%s is %s" %(number,oddity)
