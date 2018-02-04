#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
ко всем допустимым целым числам добавить ведущие нули
632 dsf 12 sdfds 743g\n3246435 76.8
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

def zero(w):
    try:
        int(w)
        return "0" + w
    except:
        return w


for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    if len(words) > 0:
        print(' '.join(zero(word) for  word in words))