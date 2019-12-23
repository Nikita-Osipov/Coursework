# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:02:55 2019

@author: Nikita
"""
from miller_rabin import miller_rabin_test
import random, math
from math import isclose

def num_p_q(frm,to):    
    a = random.randint(frm,to)
    test = miller_rabin_test(a)
    while test != True:
        a = random.randint(frm,to)
        test = miller_rabin_test(a)
    return a

def great(Fn,up,frm,to):
    e = 2 
    lst = [] 
    while len(lst) < up and e < Fn:
        great = math.gcd(e,Fn)
        if great == 1:
            lst.append(e)
        e += 1 
    n = int(up/2)
    mode = 0 
    for e in lst[::n]:
        for i in range(1,100):
            d = (i*Fn+1)/e
            if isclose(math.floor(d),d, rel_tol = 0.0000) == True:
                mode = 1
                break
        if mode == 1:
            break
        if up < 100 and mode == 0:
            up += up
            great(Fn,up)
        else:
            open_key(frm,to)
    return e,int(d)    

def open_key(frm,to):
    p = num_p_q(frm,to)
    q = num_p_q(frm,to)
    n = p*q
    Fn = (p-1)*(q-1)
    res_great = great(Fn,10,frm,to)
    return res_great[0],res_great[1],n
      
