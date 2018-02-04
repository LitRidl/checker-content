#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно выделить шестнадцатиричные целые числа без знака и напечатать шестнадцатиричную сумму их нечётных цифр
928357av -careful -dead ff 1234\nnothing\naim do 05 -150 1A beef +man -17
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import base_repr



def word_ok(w):
    return all(c in hexdigits for c in w)


def s(w):
    w = w.upper()
    return base_repr(sum(int(c, base=16) for c in w if c in '13579BDF'), base=16)


for line in stdin:
    words = [w.strip() for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if word_ok(w)]
    if len(words) > 0:
        print(*[s(w) for w in words])
