# https://open.kattis.com/problems/ladder

from sys import stdin
from math import sin, ceil, pi

h,v = map(int,stdin.read().split(' '))
print int(ceil(h/sin(v*pi/180)))
