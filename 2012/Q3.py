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
ceiling = -1
for line in range(M):
    route = sys.stdin.readline().split() 
    if(int(route[2]) > ceiling):
        ceiling = int(route[2])
    l[int(route[0])-1].routes.append([int(route[1])-1,int(route[2])])
    l[int(route[1])-1].routes.append([int(route[0])-1,int(route[2])])
def containsAll(temp):
    for i in l:
        if(not (i in temp)):
            return -1
    return 1
        
Maxs=[]
Maxs.append(ceiling)
def visitAll(Max,Visited,current):
    VCopy = list(Visited)
    VCopy.append(current)
    #print len(VCopy)    
    for nNode in current.routes:
        if(l[nNode[0]] in l and l[nNode[0]]!= current):
            #print("%d to %d" %(int(l.index(current))+1,int(nNode[0])+1))
            tempM = Max
            if(nNode[1] > Max):
                Max = nNode[1]
            if(Max < ceiling and len(VCopy) < N*2):
                current = l[nNode[0]]
                cur = visitAll(Max,VCopy,current)
                if(Max > cur and cur != None):
                    Max = cur
        if(containsAll(VCopy)):
        # print("All visited")
            Maxs.append(Max)
        Max=tempM
   # print "No route"
visitAll(-1,[],l[0])    
#f=min(Maxs)
print Maxs