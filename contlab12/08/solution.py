#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
перенести первый блок нулей из младших разрядов в середину десятичной записи числа
1234567
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

def f(s):
    i = len(s) - 1
    count = 0
    while i > (len(s)//2):
        if s[i] == '0':
            count += 1
        elif count != 0:
            break
        i -= 1
    if count == 0:
        return s
    print(s[i+1:i+1+count])
    zero = s[i+1:i+1+count]
    new_s = s[:i+1] + s[i+1+count:]
    result = new_s[:len(new_s)//2] + zero + new_s[len(new_s)//2:]
    return result


words = stdin.read().strip().split()

for word in words:
    r = f(word)
    if r == '-0':
        r = '0'
    print(r)