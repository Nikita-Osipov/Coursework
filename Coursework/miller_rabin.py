# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:05:44 2019

@author: Nikita
"""
import random    
import math                     
            
def miller_rabin(num,rnds):
    
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
        return True
        
    elif num == 4 or num == 6 or num == 8 or num == 9 or num == 10:
        return False
        
    elif num > 2 and rnds > 0:
        
        if num % 2 == 0:
            return False
            
        else:
            s = 0
            t = num - 1
            
            while t % 2 == 0:
                t //= 2
                s +=1
            
            for i in range(rnds):
                a = random.randint(2,num-2)
                x = pow(a,t,num)
                if x == 1 or x == num - 1:
                    continue               
                for j in range(s-1):
                    x = pow(x,2,num)
                    if x == num - 1:
                        break
                else:
                    return False
            return True            
    else:
        print('Неверные данные\nПервый аргумент >= 2\nВторой > 0')

#ex1 = 233644041304680072699949795023810733936348917337177642573003025647464227586924845446450732322802680267208401293264931001193901
#ex2 = 942501139121453
#num = ex2

def miller_rabin_test(num):
    s = math.ceil(math.log2(num))
    return miller_rabin(num,s)