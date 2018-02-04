#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычислить наибольший общий делитель исходных чисел.
Входное слово представляет собой два беззнаковых двоичных числа (возможно, с ведущими нулями), разделенные знаком "%".
двоичное число, наибольший общий делитель исходных чисел
10000010%101010
'''

from __future__ import print_function


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else: b = b % a
    return a + b

a, b = raw_input().split('%')

inta = long(a, base = 2)
intb = long(b, base = 2)

res = gcd(inta,intb)
print(bin(res)[2:])