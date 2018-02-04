#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Сокращение обыкновенных дроби в десятичной системе счисления.
записаны через пробел два числа - числитель и знаменатель.
два числа через пробел - числитель и знаменатель, сокращениенной дроби
15 50
'''


from __future__ import print_function

def nod(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = raw_input().strip().split()
inta = long(a)
intb = long(b)

nd = nod(inta, intb)

while (nd != 1):
    inta /= nd
    intb /= nd
    nd = nod(inta, intb)

print('{0} {1} {2} {3}'.format(a, b, inta, intb))
