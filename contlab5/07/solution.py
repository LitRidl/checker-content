#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Генерация двух чисел из разрядов двоичного числа, находящихся на четных и нечетных позициях.
записано беззнаковое число произвольной длины в двоичной системе счисления
два двоичных числа, составленных из четных и нечетных разрядов исходного числа в порядке от наименьшего разряда к наибольшему
110110110
'''
from __future__ import print_function

a = raw_input().strip()
inta = int(a)
cap = 1
lresult, rresult = "", ""
while inta > 0:
    r = str(int(inta % 10))
    if inta >= 10:
        l = str(int((inta / 10) % 10))
        lresult = lresult + l
    rresult = rresult + r 
    cap = cap * 100
    inta = int(inta / 100)

rresult = str(rresult).lstrip('0') or '0'
lresult = str(lresult).lstrip('0') or '0'

print("{0} {1} {2}".format(a, rresult, lresult))
