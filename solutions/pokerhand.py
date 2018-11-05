# https://open.kattis.com/problems/pokerhand

from sys import stdin

ranks = {}
cards = stdin.readline().rstrip("\n").split(' ')

for card in cards:
    rank = card[0]
    try:
        ranks[rank] += 1
    except KeyError:
        ranks[rank] = 1

print ranks[max(ranks, key=ranks.get)]
