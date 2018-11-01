# https://open.kattis.com/problems/r2

import sys

input = sys.stdin.read().split()
s = int(input.pop())
r = int(input.pop())
print 2*s - r
