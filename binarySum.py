#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:32:03 2019

@author: felipe
"""

#%% Soma Binária
# Funções
def binarySum(Bin1, Bin2):
    tamanhoBin1 = len(Bin1)
    tamanhoBin2 = len(Bin2)
    somaBin = []
    if (tamanhoBin1 != tamanhoBin2):
        print("Binários com tamanho diferente!")
        return
    for i in range(0, tamanhoBin1):
        if(Bin1[i] == 0 and Bin2 == 0):
            somaBin.append(0)
        if((Bin1[i] == 1 and Bin2 == 0) or (Bin1[i] == 0 and Bin2 == 1)):
            somaBin.append(1)
        if(Bin1[i] == 1 and Bin2 == 1):
            somaBin.append(0)
            somaBin.append(1)
    somaBin.reverse()
    return somaBin

# Valores

Bin1 = [1, 0, 0]

Bin2 = [1, 0, 1]

# Chamada da função

print(binarySum(Bin1, Bin2))