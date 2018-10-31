# https://open.kattis.com/problems/nastyhacks

import sys

input = sys.stdin.read().split("\n")
input.pop(0)
input.pop()

for line in input:
    (a, b, c) = line.split(' ')
    if int(a) < (int(b) - int(c)):
        print "advertise"
    elif int(a) == (int(b) - int(c)):
        print "does not matter"
    else:
        print "do not advertise"
