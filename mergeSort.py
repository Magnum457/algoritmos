#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:04:27 2019

@author: felipe
"""

#%% Merge Sort

# imports
import math as m

# funções
def mergeSort(Array):
    print("Dividindo o array")
    if (len(Array) > 1):
        meio = len(Array) // 2
        ladoEsquerdo = Array[:meio]
        ladoDireito = Array[meio:]
        
        mergeSort(ladoEsquerdo)
        mergeSort(ladoDireito)
        
        # inicializando as variaveis auxiliares
        i = 0
        j = 0
        k = 0
        
        # juntando os vetores já organizados
        while i < len(ladoEsquerdo) and j < len(ladoDireito):
            if (ladoEsquerdo[i] < ladoDireito[j]):
                Array[k] = ladoEsquerdo[i]
                i = i + 1
            else:
                Array[k] = ladoDireito[j]
                j = j + 1
            k = k + 1
            
        # percorrendo os valores que sobraram nos vetores
        while i < len(ladoEsquerdo):
            Array[k] = ladoEsquerdo[i]
            i = i + 1
            k = k + 1
            
        while j < len(ladoDireito):
            Array[k] = ladoDireito[j]
            j = j + 1
            k = k + 1
            
        print("Agrupando ", Array)

# valores
Sequencia = [5, 3, 4, 1, 2, 6]

# chamada de função
mergeSort(Sequencia)

# print
print(Sequencia)
