# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 19:44:03 2019

@author: Nikita
"""

from Alphabet import ru_code, en_code, ru_en_code

def ru_dict_simple():
    a = ru_code()
    b = []
    for i in range(1,len(a)+1):
        b.append(str(i))
    return dict(zip(a,b))

def en_dict_simple():
    a = en_code()
    b = []
    for i in range(1,len(a)+1):
        b.append(str(i))
    return dict(zip(a,b))

def ru_en_dict_simple():
    a = ru_en_code()
    b = []
    for i in range(1,len(a)+1):
        b.append(str(i))
    return dict(zip(a,b))
    
def reverse_ru_dict_simple():
    dct = ru_dict_simple()
    dct = dict(zip(dct.values(), dct.keys()))
    return dct

def reverse_en_dict_simple():
    dct = en_dict_simple()
    dct = dict(zip(dct.values(), dct.keys()))
    return dct

def reverse_ru_en_dict_simple():
    dct = ru_en_dict_simple()
    dct = dict(zip(dct.values(), dct.keys()))
    return dct

def ru_file_simple(file1,file2,e,n):
    b = ''
    a = open(file1,'r')
    for line in a:
        lst = list(line)
        for i in lst:
            try:
                c = int(ru_dict_simple()[i])
                c = pow(c,e,n)
                #c = c**e % n
                b = b + str(c)+'a'
            except Exception:
                b = b + 'Eara'
    a.close()
    f = open(file2,'w')
    f.write(b)
    f.close()
    
def en_file_simple(file1,file2,e,n):
    b = ''
    a = open(file1,'r')
    for line in a:
        lst = list(line)
        for i in lst:
            try:
                c = int(en_dict_simple()[i])
                c = pow(c,e,n)
                #c = c**e % n
                b = b + str(c)+'a'
            except Exception:
                b = b + 'Eara'
    a.close()
    f = open(file2,'w')
    f.write(b)
    f.close()
    
def ru_en_file_simple(file1,file2,e,n):
    b = ''
    a = open(file1,'r')
    for line in a:
        lst = list(line)
        for i in lst:
            try:
                c = int(ru_en_dict_simple()[i])
                c = pow(c,e,n)
                #c = c**e % n
                b = b + str(c)+'a'
            except Exception:
                b = b + 'Eara'
    a.close()
    f = open(file2,'w')
    f.write(b)
    f.close()
    
    
#ru_en_file_simple('testTXT.txt','test2.txt',5,5561)
#print(ru_en_dict_simple())