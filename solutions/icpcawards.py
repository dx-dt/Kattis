# https://open.kattis.com/problems/icpcawards

from sys import stdin

universities,teams = [],[]

for line in stdin.readlines()[1:]:
    if len(universities) < 12:
        university, team = line.rstrip("\n").split(' ')
        if university not in universities:
            universities.append(university)
            teams.append(team)

for i in range(len(universities)):
    print "%s %s" % (universities[i], teams[i])
