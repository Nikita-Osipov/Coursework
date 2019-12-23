# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:23:23 2019

@author: Nikita
"""
import math

def ibn_al_banna(x):
    k = 0 
    s = math.floor(math.sqrt(x))
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    elif x == 1:
        return False
    else:
        for i in range(2,s+1):
            if x % i == 0:
                k = 1
                return False
                break                              
            else:
                continue
    if k == 0:
        return True
    
#print(ibn_al_banna(64219804625359))