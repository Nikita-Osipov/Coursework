# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:08:13 2019

@author: Nikita
"""

from miller_rabin import miller_rabin_test
import random, time

def big_prime(frm,to):    
    a = random.randint(frm,to)
    test = miller_rabin_test(a)
    while test != True:
        a = random.randint(frm,to)
        test = miller_rabin_test(a)
    return a


def time_of(frm,to):   
    a = time.time()
    res = big_prime(frm,to)
    b = time.time()
    print('Случайное вероятно простое число: '+str(res)+'\nВремя вычисления: '+str(b - a))