# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:18:36 2017

@author: Gearoid
"""

import sys
import math

N=0
M=0
line  = sys.stdin.readline()
for n in line.split():
    if(N==0):
        N=int(n)
    else:
        M=int(n)


socks = []

for s in sys.stdin:
    toup = []
    for n in s.split():
        toup.append(int(n))
    socks.append(toup)
        

print socks
        
        
#Color :: 0 --> M
def sockDiff(sc,sh,tc,th):
    return math.sqrt(pow(sc-tc,2)+pow(sh-th,2))

while(len(socks) > 0):
    sockMin = sys.maxint
    sock1Min = [-1,-1]
    sock2Min = [-1,-1]
    for sock1 in socks:
        for sock2 in socks:
            if(sock1 != sock2):
                cont = sockDiff(sock1[0],sock1[1],sock2[0],sock2[1])
                if(cont < sockMin):
                    sockMin = cont
                    sock1Min = sock1
                    sock2Min = sock2
    socks.remove(sock1Min)
    socks.remove(sock2Min)
    if(sock1Min[0] > sock2Min[0]):
        temp = sock1Min
        sock1Min = sock2Min
        sock2Min = temp
    elif(sock1Min[0] == sock2Min[0]):
        if(sock1Min[1] > sock2Min[1]):
            temp = sock1Min
            sock1Min = sock2Min
            sock2Min = temp    
    print "%d %d %d %d" % (sock1Min[0], sock1Min[1], sock2Min[0], sock2Min[1])
                
                