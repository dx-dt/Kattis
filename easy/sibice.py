# https://open.kattis.com/problems/sibice

import sys
import math

input = sys.stdin.readline().split(' ')
input.pop(0)
w = int(input.pop(0))
h = int(input.pop(0))
diagonal = math.sqrt(w*w+h*h)
matches = sys.stdin.read().split()

for match in matches:
    if float(match) > diagonal:
        print 'NE'
    else:
        print 'DA'
