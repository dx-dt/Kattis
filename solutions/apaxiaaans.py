# https://open.kattis.com/problems/apaxiaaans

from sys import stdin

name = stdin.readline().rstrip("\n")

output = ''
last_char = None

for char in name:
    if char == last_char:
        continue
    else:
        last_char = char
        output += char

print output
