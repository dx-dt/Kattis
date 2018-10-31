# https://open.kattis.com/problems/autori

import sys

short = ''
for name in sys.stdin.read().split('-'):
    short += name[0]
print short
