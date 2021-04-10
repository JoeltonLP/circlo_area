#!/usr/bin/python3
# circle_area_v8

from math import pi

raio = input('Raio: ')


def return_circle_area(raio):
    circle_area = pi * float(raio) ** 2

    return circle_area


circle_area = return_circle_area(raio)


print(circle_area)
