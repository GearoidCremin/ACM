# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:17:11 2017

@author: gearoid
"""
import sys
import math

num = sys.stdin.next()

l=[]
maxp = [-1,-1]
minp = [sys.maxint,sys.maxint]
for line in sys.stdin:
    point = line.split()
    point = [float(point[0]),float(point[1])]
    if(point[0] < minp[0]):
        minp = point
    if(point[0] > maxp[0]):
        maxp = point
    l.append(point)

def distance(p1,p2):
    return math.sqrt(pow(p1[0]-p2[0],2)+pow(p1[1]-p1[1],2))

def slope(p1,p2):
    if(p2[0] - p1[0] == 0):
        return 0
    else:
        return (p2[1]-p1[1])/(p2[0]-p1[0])
    
m=slope(minp,maxp)
c=m*(0-minp[0])+minp[1]

def partLine(point):
    
    y = m*point[0]+c
    if(point[1] > y):
        return 1
    else:
        return -1

wish_list = sorted(l,key = lambda l:l[0])
wish_list.remove(minp)
wish_list.remove(maxp)

rlist = []
llist=[]

for num in wish_list:
    if(partLine(num)==1):
        rlist.append(num)
    else:
        llist.append(num)
        
llist = sorted(llist,key = lambda llist:llist[0])
rlist = sorted(rlist,key = lambda rlist:rlist[0])
rlist.reverse()

total = 0.0
current = minp
while(len(llist) > 0):
    total+= distance(llist[0], current)
    print "%s to %s" %(current, llist[0])    
    current=llist[0]
    llist.remove(llist[0])
    
total+=distance(current,maxp)
print "%s to %s" %(current,maxp)
current = maxp

while(len(rlist) > 0):
    total+= distance(rlist[0], current)
    print "%s to %s" %(current, rlist[0])       
    current=rlist[0]
    rlist.remove(rlist[0])
    
total+=distance(current,minp)
print "%s to %s" %(current, minp)       
    
print "%.2f" %total