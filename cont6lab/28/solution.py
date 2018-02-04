#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Поразрядная конъюнкция двух двоичных чисел (слова разной длины, дополняются 0 слева).
через пробел записаны два беззнаковых числа произвольной длины в двоичной системе счисления.
двоичное число, полученное путем конъюнкции чисел, без удаления ведущих нулей
0011 10101110
'''

from __future__ import print_function


def con(a, b):
    rez = ""
    for i in range(len(a)):
        if (a[i] == "1" or b[i] == "1"):
            rez += "1"
        else:
            rez += "0"
    return rez

a, b = raw_input().split()
result = 0


if (len(a) < len(b)):
    result = con(a.rjust(len(b), "0"), b)
elif (len(a) > len(b)):
    result = con(a, b.rjust(len(a), "0"))

print('{0} {1} {2}'.format(a, b, result))
