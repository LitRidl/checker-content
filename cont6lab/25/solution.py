#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Выделение разрядов первого двоичного числа по маске, задаваемой вторым числом.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления
двоичное число, содержащее последовательность цифр первого числа, выделенные по маске с сохранением ведущих нулей
11010 111011
'''

from __future__ import print_function

a, b = raw_input().split()
maxlen = max(len(a), len(b))

newa = a.zfill(maxlen)
newb = b.zfill(maxlen)

temp = [x for x, y in zip(newa, newb) if y == '1']

result = ''.join(temp)

print('{0} {1} {2}'.format(a, b, result))
