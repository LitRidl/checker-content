#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Кодирование первого слова по коду Цезаря с ключом, равным второму слову.
Входное слово представляет собой последовательность малых латинских букв a-z, за которой следует двоичное число.
исходное слово, закодированное по Цезарю с заданным ключом
hellobaby 10
'''

from __future__ import print_function

alpha = 'abcdefghijklmnopqrstuvwxyz'
a = raw_input()
i = 0
for c in a:
    if c in alpha:
        i += 1
    else:
        break
str = a[:i]
key = a[i:]


res = ''
for c in str:
    res += alpha[(alpha.index(c) + int(key)) % len(alpha)]
print(res)
