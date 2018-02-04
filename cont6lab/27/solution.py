#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление поразрядной дизъюнкции двух двоичных чисел (слова одинаковой длины).
через пробел записаны два беззнаковых числа одинаковой длины в двоичной системе счисления.
двоичное число, полученное путем дизъюнкции исходных чисел, без удаления ведущих нулей
1010110100 0010111000
'''

from __future__ import print_function


def diz(a, b):
    rez = ""
    for i in range(len(a)):
        if (a[i] == "1" or b[i] == "1"):
            rez += "1"
        else:
            rez += "0"
    return rez


a, b = raw_input().split()

result = diz(a, b)

print('{0} {1} {2}'.format(a, b, result))
