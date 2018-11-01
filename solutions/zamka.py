# https://open.kattis.com/problems/zamka

from sys import stdin

L, D, X = map(int, stdin.read().rstrip("\n").split("\n"))

for N in range(L,D+1):
    sum = 0
    for i in str(N):
        sum += int(i)
    if sum == X:
        print N
        break

for N in reversed(range(L,D+1)):
    sum = 0
    for i in str(N):
        sum += int(i)
    if sum == X:
        print N
        break
