#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:13:17 2024

@author: annette
"""

import math
def gcd(a, b):
    if b>a:
        new = a
        a = b 
        b = new
    if b == 0:
        return a 
    else: 
        return gcd(b, (a%b))
def remove_pairs(path):
    if len(path) < 2:
        return path
    else:
        i = 0  
        while i < len(path) - 1:  
            first, second = path[i], path[i+1]
            if (first == "E" and second == "W") or (first == "W" and second == "E")or\
            (first == "N" and second == "S") or (first == "S" and second == "N"):
                path = path[:i] + path[i+2:]
                return remove_pairs(path)
            i += 1
        return path 
def bisection_root(function, x1, x2):
    y1 = function(x1)
    y2 = function(x2)
    if (y1<0 and y2<0) or (y1>0 and y2>0):
        raise ValueError("cannot find root with solutions being on same side of x")
    if y1<= 0.001 and y1>=-0.001:
        return x1
    if y2<= 0.001 and y2>=-0.001:
        return x2
    new_val = (x1+x2)/2
    newy = function(new_val)
    if newy * y1 < 0:
        return bisection_root(function, new_val, x1)
    return bisection_root(function, new_val, x2)