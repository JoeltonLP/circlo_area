#!/usr/bin/python3

# circle_area_v9 Arguments on command line

from math import pi
import sys

raio = sys.argv[1]


def return_circle_area(raio):
    circle_area = pi * float(raio) ** 2

    return circle_area


circle_area = return_circle_area(raio)


print('Circle area: ', circle_area)
