# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 18:54:54 2017

@author: Gearoid
"""
import sys

s = sys.stdin.readline()
N = int(s)

l=[]

for n in range(N):
    s=sys.stdin.readline()
    s=s.split()
    l.append([float(s[0]),float(s[1])])
l=sorted(l, key = lambda l:l[0] )
print l

def slope(p1,p2):
    return (p2[1]-p1[0])/(p2[0]-p1[0])

def highLow(p1,p2,test):
    m=slope(p1,p2)
    y=m*(test[0]-p1[0])+p1[1]
    if(y==test[1]):
        return 0
    elif(y > test[1]):
        return 1
    else:
        return -1
        
def overUnder(p1,p2,superset,ou):
    for point in superset:
        check = highLow(p1,p2,point)
        if(check != ou and point != p1 and point != p2):
            return -1
    return 1

