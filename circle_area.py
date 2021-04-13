#!/usr/bin/python3
import sys

from math import pi


def area_circle(raio):
    raio = pi * float(raio) ** 2
    return raio


def help():
    print('needs an argument\n')
    print('sintaxe:')
    print('use: {} <raio>\n' .format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        area = area_circle(sys.argv[1])
        print('Area Circle: {:.2f}' .format(area))
