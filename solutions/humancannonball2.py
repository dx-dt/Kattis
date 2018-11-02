# https://open.kattis.com/problems/humancannonball2

from sys import stdin
from math import pi, cos, sin

def parse_input(line):
    return map(float,line.rstrip("\n").split(' '))

def to_radians(angle):
    return angle*pi/180

def calc_time(v, theta, x):
    return x/(v*cos(theta))

def calc_height(v, t, theta):
    g = 9.81 # gravitational acceleration
    return v*t*sin(theta) - 0.5*g*t**2

def check_safety(h_b,h_1,h_2):
    m = 1.0 # security margin
    if (h_b >= h_1 + m) and (h_b <= h_2 - m):
        print "Safe"
    else:
        print "Not Safe"

for line in stdin.readlines():
    # skip first line
    if len(line) <= 4:
        continue

    v_0, theta, x_1, h_1, h_2 = parse_input(line)
    theta = to_radians(theta)
    t =  calc_time(v_0, theta, x_1)
    h_b = calc_height(v_0, t, theta)
    check_safety(h_b, h_1, h_2)
