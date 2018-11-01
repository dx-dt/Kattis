# https://open.kattis.com/problems/trik

from sys import stdin

cups = [1,0,0]

for char in stdin.readline().rstrip("\n"):
    if char == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    if char == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    if char == 'C':
        cups[0], cups[2] = cups[2], cups[0]

for i in range(len(cups)):
    if cups[i] == 1:
        print i+1
