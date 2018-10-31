# https://open.kattis.com/problems/datum

from sys import stdin

day_in,month_in = map(int,stdin.readline().rstrip("\n").split(' '))

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
weekdays =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
year_offset = 2
total_days = 0

for month in range(month_in-1):
    total_days += days_in_month[month]

total_days += day_in
weekday_number = (total_days + year_offset) % 7

print weekdays[weekday_number]
