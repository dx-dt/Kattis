# https://open.kattis.com/problems/spavanac

import sys

input = sys.stdin.read().split()
h = int(input[0])
m = int(input[1])

if m >= 45:
    print h,m-45
else:
    print (h-1)%24,(m-45)%60
