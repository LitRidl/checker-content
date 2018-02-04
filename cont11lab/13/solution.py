#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
у всех допустимых 16-ричных чисел перенести ведущие нули в младшие разряды слова фиксированной длины
-00014a h12 +00A 0ABCD  67500 00m\nsdgdf 1fdh 10e
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

def raz(w):
    a = ""
    try:
        int(w, base=16)
        n = 0
        if (w[0] == "+" or w[0] == "-"):
            a = w[0]
            w = w[1:]
        while (w[n] == "0" and n != len(w) - 1):
            n += 1
        return a + w[n:] + "0" * n
    except:
        return a + w


for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    if len(words) > 0:
        print(' '.join(raz(word) for  word in words))
