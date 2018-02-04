#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Выделение разрядов второго двоичного числа по маске, заданной первым числом.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления
двоичное число, содержащее последовательность цифр второго числа, выделенные по маске с сохранением ведущих нулей
111011 11010 
'''
from __future__ import print_function

a, b = raw_input().split()
maxlen = max(len(a), len(b))

newa = a.zfill(maxlen)
newb = b.zfill(maxlen)

temp = [y for x, y in zip(newa, newb) if x == '1']

result = ''.join(temp)

print('{0} {1} {2}'.format(a, b, result))

