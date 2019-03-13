#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:55:41 2019

@author: felipe
"""

#%% Busca linear
# Funções
def linearSearch(Lista, valor):
    # guardando o tamanho do vetor
    tamanhoLista = len(Lista)
    i = 0
    # percorrendo e comparando os valores do vetor com o vetor passado
    while(i < tamanhoLista and Lista[i] != valor):
        i = i + 1
    # verificando se o valor foi achado ou não
    if (i < tamanhoLista):
        i = i + 1
        return "O valor " + str(valor) + " se encontra na posição " + str(i)
    else:
        return "Valor não encontrado"

# Valores
Lista = [4, 7, 2, 8, 5, 10]

Valor = 5

# Chamada das funções
print(linearSearch(Lista, Valor))