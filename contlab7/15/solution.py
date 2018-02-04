#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Выделение разрядов первого числа по маске, в качестве которой используется второе число.
Входное слово представляет собой два беззнаковых двоичных числа (возможно, с ведущими нулями), разделенные знаком "$".
двоичное число, результат выделения по маске
11000011$100111111
'''

from __future__ import print_function

a, b = raw_input().split('$')
maxlen = max(len(a), len(b))

newa = a.zfill(maxlen)
newb = b.zfill(maxlen)

temp = [x for x, y in zip(newa, newb) if y == '1']

result = ''.join(temp)

print (result)