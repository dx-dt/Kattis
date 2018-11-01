# https://open.kattis.com/problems/bela

from sys import stdin

points = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
dom_points = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}

score = 0

dom_suit = stdin.readline().rstrip("\n").split(' ')[1]

for line in stdin.readlines():
    rank,suit = line.rstrip("\n")[:]
    if suit == dom_suit:
        score += dom_points[rank]
    else:
        score += points[rank]

print score
