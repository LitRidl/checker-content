#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
подсчитать число слов в однострочных комментариях (//) в программе на Си
#include <stdio.h>\n// first comment\nint main(void)\n{\n    int a = 5, b = 10;\n    printf("%d", a + b); // second comment ...\n    return 0;\n}
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

res = 0

for i in stdin.readlines():
    count_quotes = 0
    count_slash = 0
    comment = ""
    for j in range(len(i)):
        if (i[j] == "\""):
            count_quotes += 1
            count_slash = 0
        elif (i[j] == "/" and count_quotes % 2 == 0):
            count_slash += 1
        else:
            count_slash = 0
        if (count_slash == 2):
            comment = i[j:]
            break
    try:
        comment = comment[1:]
    except:
        pass
    res += len(comment.split())

print(res)
