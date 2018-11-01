# https://open.kattis.com/problems/everywhere

from sys import stdin

number_of_sets = int(stdin.readline().rstrip("\n"))

for n in range(number_of_sets):
    length_of_set = int(stdin.readline().rstrip("\n"))
    unique_cities = set()

    for m in range(length_of_set):
        city = stdin.readline().rstrip("\n")
        unique_cities.add(city)

    print len(unique_cities)
