#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Генерация двух чисел из четных и нечетных разрядов двоичного числа.
записано беззнаковое число произвольной длины в двоичной системе счисления
два двоичных числа, записанных через пробел, первое число составить из четных разрядов, второе -- из нечетных разрядов исходного числа; если одного из чисел нет, то выводить одно число
110110110
'''

from __future__ import print_function

a = raw_input().strip()
nullCount = a.count("0")
oneCount = a.count("1")
nullRes = "0" * nullCount
oneRes = "1" * oneCount

if nullRes == "":
    print("{0} {1}".format(a, oneRes))
elif oneRes == "":
    print("{0} {1}".format(a, nullRes))
else:
    print("{0} {1} {2}".format(a, nullRes, oneRes))
