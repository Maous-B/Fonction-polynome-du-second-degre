#!usr/bin/env python3
from lycee import *
from math import *
import sys
print("ax² + bx + c")
a = input("Entrez a :")
b = input("Entrez b :")
c = input("Entrez c :")

print(a + "x²" + b + "x" + c)
delta = int(b)*int(b) - 4 * int(a) * int(c)
print(delta)
if delta > 0:
    print("La fonction admet deux racines")
    premieresolution = (b-sqrt(delta)) / 2 * a
    deuxiemesolution = (b+sqrt(delta)) / 2 * a
    print("x1 = " + premieresolution)
    print("x2 = " + deuxiemesolution)
if delta < 0:
    print("La fonction n'admet aucune racines")
    sys.exit()
if delta == 0:
    print("La fonction admet une racine")
