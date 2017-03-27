# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:50:59 2017

@author: gearo
"""
import sys
N=0
X=[]
for s in sys.stdin.readline():
    for n in s.split():
        N=int(n)
s = sys.stdin.readline()
for n in s.split():
    X.append(int(n))
    
sumFree = True
for num in X:
    for i in range(len(X)):
        for j in range(len(X)):
            if((X[i] + X[j]) == num and i != j):              
                print 0
                exit()
print 1