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
        
randInts = []

for n in range(int(l[0])):
    randInts.append(int(l[n+1]))
           

for current in randInts:
    left =0
    right =0
    while(current != 0):
        if(current%2==0):
            left += 1
        else:
            right +=1
        current = current/2
        
    if(left > right):
        print -1
    elif (right > left):
        print 1
    else:
        print 0