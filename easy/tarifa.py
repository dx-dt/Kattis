# https://open.kattis.com/problems/tarifa

import sys

input = sys.stdin.read().split()
quota = int(input.pop(0))
months = int(input.pop(0))
usages = input[:months]
left = 0

for usage in usages:
    left += quota - int(usage)

print left + quota
