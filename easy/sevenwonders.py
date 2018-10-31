# https://open.kattis.com/problems/sevenwonders

import sys

score = 0
cards = {'T': 0, 'C': 0, 'G': 0}

for card in sys.stdin.read().rstrip()[:]:
    cards[card] += 1

for key in cards.keys():
    score += cards[key]**2

while cards['T'] > 0 and cards['C'] > 0 and cards['G'] > 0:
    score += 7
    for key in cards.keys():
        cards[key] -= 1

print score
