#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:13:17 2024

@author: annette
"""

#problem 1
def gcd(a, b):
    if b>a:
        new = a
        a = b 
        b = new
    if b == 0:
        return a 
    else: 
        return gcd(b, (a%b))
    
    
#problem 2 - we slayed it!! 
def remove_pairs(path):
    if len(path)==0 or len(path)==1:
        return path 
    first, rest = path[0],path[1:]
    if {(first== "E" and rest[0] == "W" ) or (first== "W" and rest[0] == "E" ) or 
    (first== "N" and rest[0] == "S" ) or (first== "S" and rest[0] == "N" )}:
        return remove_pairs(rest[1:])
    else:
        return first + remove_pairs(rest)
    
    
#problem 3
def bisection_root(function, x1, x2):
    y1 = function(x1)
    y2 = function(x2)
    if y1<0 and y2<0:
        raise ValueError("cannot find root with solutions being on same side of x")
    if y1>0 and y2>0:
        raise ValueError("cannot find root with solutions being on same side of x")
    if y1<= 0.001 or y1>=0.001:
        return x1
    if y2<= 0.001 or y2>=0.001:
        return x2
    else:
        new_val = (x1+x2)/2
        if new_val * x1 < 0:
            return bisection_root(function, new_val, x2)
        if new_val * x2 < 0:
            return bisection_root(function, new_val, x2)
    
    
    
    
    
        
        
    