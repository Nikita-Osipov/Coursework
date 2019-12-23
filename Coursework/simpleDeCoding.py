# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:08:52 2019

@author: Nikita
"""

from simpleCoding import reverse_ru_dict_simple, reverse_en_dict_simple,reverse_ru_en_dict_simple

def decoding_ru_simple(file2,file3,d,n):
    end = []
    b = ''
    a = open(file2,'r')
    for line in a:
        b = b + line
    a.close()
    b = b.split('a')
    c = []
    for j in b:
        try:
            t = pow(int(j),d,n)
            #t = int(j)**d % n
            c.append(t)
        except Exception:
            c.append(j)
    for i in c:
        try:
            end.append(reverse_ru_dict_simple()[str(i)])
        except Exception:
            end.append(str(i))
    answ = ''.join(end)
    answer = open(file3,'w')
    answer.write(answ)
    answer.close()
    
def decoding_en_simple(file2,file3,d,n):
    end = []
    b = ''
    a = open(file2,'r')
    for line in a:
        b = b + line
    a.close()
    b = b.split('a')
    c = []
    for j in b:
        try:
            t = pow(int(j),d,n)
            #t = int(j)**d % n
            c.append(t)
        except Exception:
            c.append(j)
    for i in c:
        try:
            end.append(reverse_en_dict_simple()[str(i)])
        except Exception:
            end.append(str(i))
    answ = ''.join(end)
    answer = open(file3,'w')
    answer.write(answ)
    answer.close()
    
def decoding_ru_en_simple(file2,file3,d,n):
    end = []
    b = ''
    a = open(file2,'r')
    for line in a:
        b = b + line
    a.close()
    b = b.split('a')
    c = []
    for j in b:
        try:
            t = pow(int(j),d,n)
            #t = int(j)**d % n
            c.append(t)
        except Exception:
            c.append(j)
    for i in c:
        try:
            end.append(reverse_ru_en_dict_simple()[str(i)])
        except Exception:
            end.append(str(i))
    answ = ''.join(end)
    answer = open(file3,'w')
    answer.write(answ)
    answer.close()
  
#decoding_ru_en_simple('test2.txt','test3.txt',2165,5561)
