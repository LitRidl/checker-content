#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Обмен местами разрядов двоичного числа, находящихся на чётных и нечётных позициях.
записано беззнаковое число произвольной длины в двоичной системе счисления
двоичное число после обмена разрядов
11011
'''

from __future__ import print_function


a = raw_input().strip()
inta = long(a)
cap = 1
result = 0
while inta > 0:
	l = (inta / 10) % 10
	r = inta % 10
	result = result + cap * l + 10 * cap * r
	cap = cap * 100
	inta = inta / 100


print("{0} {1}".format(a, result))
