#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление наибольшего общего делителя двух чисел в десятичной системе счисления.
через пробел записаны два целых числа произвольной длины в десятичной системе счисления, возможно с ведущими нулями
число в десятичной системе счисления
1598534 908
'''

from __future__ import print_function

def nod(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = raw_input().strip().split()

inta = long(a)

intb = long(b)

result = nod(inta, intb)

print('{0} {1} {2}'.format(a, b, result))
