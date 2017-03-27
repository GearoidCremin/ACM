# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:36:04 2017

@author: Gearoid
"""

import sys

s = sys.stdin.readline()
R = int(s)

ports = []
routes = []
opts = []
ships = []

for n1 in range(R):

    reg = sys.stdin.readline()
    reg = reg.split()
    ports.append(int(reg[0]))
    ships.append(int(reg[3]))

    subroute = []
    for n2 in range(int(reg[1])):
        route = sys.stdin.readline()
        route = route.split()
        subroute.append([int(route[0]),int(route[1])])
    routes.append(subroute)
    
    subrouteopt = []
    for n2 in range(int(reg[2])):
        routeopt = sys.stdin.readline()
        routeopt = routeopt.split()
        subrouteopt.append([int(routeopt[0]),int(routeopt[1])])
    opts.append(subrouteopt)
    
