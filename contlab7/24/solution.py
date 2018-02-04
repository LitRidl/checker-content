#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Умножение двух неотрицательных целых чисел в алфавите {|}.
Входное слово представляет собой два неотрицательных целых числа в алфавите {|}.
слово в алфавите {|}, произведение исходных слов
||||||*|||
'''

from __future__ import print_function

a, b = raw_input().split('*')

alen = len(a)
blen = len(b)
res = '|' * alen * blen

print(res)