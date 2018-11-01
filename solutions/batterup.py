# https://open.kattis.com/problems/batterup

from sys import stdin

n = int(stdin.readline().rstrip("\n"))
bats = map(int, stdin.readline().rstrip("\n").split(' '))

valid_bats = 0.0
bases = 0.0

for bat in bats:
    if bat == -1:
        continue
    else:
        valid_bats += 1
        bases += bat

print bases/valid_bats
