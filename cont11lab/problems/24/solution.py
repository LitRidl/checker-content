#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
подсчитать количество восьмиричных чисел находящихся в диапазоне от 10 до 1000
7532 923746 hdbf 234av\n1252 -256 457
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

def check(w):
    try:
        a = int(w, base = 8)
        if (10 <= a <= 1000):
            return True
    except:
        pass
    return False

words = [w for w in stdin.read().split() if len(w.strip()) > 0]

res = 0

for i in words:
    if check(i):
        res += 1

print(res)
