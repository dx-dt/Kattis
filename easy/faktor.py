# https://open.kattis.com/problems/faktor

import sys

input = sys.stdin.read().split()
articles = int(input[0])
impact = int(input[1])

print articles * impact - (articles - 1)
