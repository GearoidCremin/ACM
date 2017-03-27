# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:17:21 2017

@author: gearo
"""

import sys
import math

def is_prime(n):
    if(n==1 or n==4):
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

ulo = []
s = sys.stdin.readline()
for n in s.split():
    ulo.append(int(n))

startingList=[]
primes=[]
for num in range(ulo[0],ulo[1]+1):
    if(is_prime(num)):
        startingList.append(num)
if(ulo[2] == 0):
    string = ""
    for tp in startingList:
        string+=str(tp)
        string+= " "
    print string
else:
    for i in range(ulo[2]):
        for num in range(len(startingList)):
            if(is_prime(num+1)):
                primes.append(startingList[num])
        startingList = primes
        primes=[]
    string=""
    for pr in startingList:
        string+=str(pr)
        string+= " "
    print string
