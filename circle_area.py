#!/usr/bin/python3

# Um pouco sobre módulo.
from math import pi

# Adicionando uma entrada do usário.
if __name__ == '__main__':
    raio = input('Raio: ')
    circlo_area = pi * float(raio) ** 2
    print(circlo_area)

print(dir('__main__'))
