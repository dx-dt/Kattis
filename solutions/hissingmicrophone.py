# https://open.kattis.com/problems/hissingmicrophone

from sys import stdin, exit

last = None
for letter in stdin.readline()[:]:
    if letter == 's' and last == 's':
        print 'hiss'
        exit(0)
    last = letter
print 'no hiss'
