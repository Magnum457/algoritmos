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
def mergeSort(A, inicio, fim):
    if (inicio < fim):
        meio = m.floor( (inicio + fim)/2 )
        mergeSort(A, inicio, meio)
        mergeSort(A, meio + 1, fim)
        merge(A, inicio, meio, fim)
        return A
    
def merge(A, inicio, meio, fim):
    