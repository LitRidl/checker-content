#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно выделить предпоследнее десятичное число и распечатать его цифры в системах счисления с основаниями 3, 7 и 11 (как BCD, только другие основания системы счисления)
928357av -careful 1234\nnothing\naim do 05 -150 man -19
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def word_ok(w):
    if w[0] in '+-':
        w = w[1:]
    return all(c in digits for c in w)


m = {
    3: ['000', '001', '002', '010', '011', '012', '020', '021', '022', '100'],
    7: ['00', '01', '02', '03', '04', '05', '06', '10', '11', '12'],
    11: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
}


def digs(w, base):
    if w[0] in '+-':
        w = w[1:]
    res = ''
    for c in w:
        res += m[base][int(c, base=10)]
    return res


for line in stdin:
    words = [w.strip() for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if word_ok(w)]
    if len(words) >= 2:
        ans = words[-2]
        print(digs(ans, 3), digs(ans, 7), digs(ans, 11))
