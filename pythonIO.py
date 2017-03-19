# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:26:04 2017

@author: Gearoid
"""

import sys

l=[]

for s in sys.stdin:
    for n in s.split():
        l.append(n)

print l
        