# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 01:23:16 2019

@author: Nikita
"""
import string

def en_code():
    en = list(string.printable)
    return en

def ru_code():
    ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ru = ru + ru.upper()+(string.printable)[:10]+(string.printable)[62:]
    return list(ru)

def ru_en_code():
    en = list(string.printable)
    ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ru = ru + ru.upper()
    ru = list(ru)
    return ru + en
    
#print(ru_en_code())