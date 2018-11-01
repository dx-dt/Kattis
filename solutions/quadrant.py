# https://open.kattis.com/problems/quadrant

import sys

input = sys.stdin.read().split()
x = int(input[0])
y = int(input[1])

if x > 0 and y > 0:
    print 1
elif x < 0 and y > 0:
    print 2
elif x < 0 and y < 0:
    print 3
else:
    print 4
