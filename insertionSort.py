#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:47:05 2019

@author: felipe
"""
#%% Insertion Sort 
# Funções
def insertionSort(Lista):
    # pegando o tamanho do array
    tamanhoLista = len(Lista)
    # loop para percorrer o array a partir do segundo número
    for j in range(1, tamanhoLista):
        # guardando o valor atual em uma varivel para comparar ela com as anteriores
        aux = Lista[j]
        i = j - 1
        # loop para voltar até o inicio do array comparando com a variavel aux
        while(i >= 0 and Lista[i] > aux):
            Lista[i + 1] = Lista[i] # passa os valores maiores uma posição a frente
            i = i - 1 
        Lista[i + 1] = aux # guarda o valor aux na posição desejada
    return Lista

# Valores
Sequencia = [5,2,4,6,1,3];

Sequencia2 = [31, 41, 59, 26, 41, 58];

# Chamadas de funções

SequenciaOrdenada = insertionSort(Sequencia)
SequenciaOrdenada2 = insertionSort(Sequencia2)

print(SequenciaOrdenada)
print(SequenciaOrdenada2)
#%% Insertion Sort decrescente
# Funções
def insertionSortDesc(Lista):
    #pegando o tamanho da lista
    tamanhoLista = len(Lista)
    #loop para percorrer o array a parti do segundo número
    for j in range(1, tamanhoLista):
        # guardando o valor atual em uma variavel para coparar ela com as anteriores
        aux = Lista[j]
        i = j - 1
        #loop para voltar até o inicio do array comparando com a variavel aux
        while(i >= 0 and Lista[i] < aux):
            Lista[i + 1] = Lista[i]
            i = i - 1
        Lista[i + 1] = aux
    return Lista

# Valores
Sequencia = [5,2,4,6,1,3];

Sequencia2 = [31, 41, 59, 26, 41, 58];

# Chamadas de funções

SequenciaOrdenada = insertionSortDesc(Sequencia)
SequenciaOrdenada2 = insertionSortDesc(Sequencia2)

print(SequenciaOrdenada)
print(SequenciaOrdenada2)