# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:02:37 2017

@author: gearo
"""
import sys

s= sys.stdin.readline()
s=s.split()
N=int(s[0])
M=int(s[1])
    
l=[]

class Tree():
    def __init__(self):
        self.routes = []

for port in range(N):
    l.append(Tree())

for line in range(M):
    route = sys.stdin.readline().split() 
    l[int(route[0])-1].routes.append([int(route[1])-1,int(route[2])])
    l[int(route[1])-1].routes.append([int(route[0])-1,int(route[2])])


def visitAll(Max,Visited,current):
    VCopy = list(Visited)
    VCopy.remove(current)    
    for nNode in current.routes:
        if(l[nNode[0]] in VCopy):
            if(nNode[1] > Max):
                Max = nNode[1]
            if(len(VCopy) > 0):
                current = l[nNode[0]]
                cur = visitAll(Max,VCopy,current)
                print cur
                if(Max > cur):
                    Max = cur
    return Max
v = l
f=visitAll(-1,v,l[0])    
print "Minimum cost is %d" %f