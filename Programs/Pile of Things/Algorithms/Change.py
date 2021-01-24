#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author Details
# =============================================================================
__author__ = 'Chet Coenen'
__copyright__ = 'Copyright 2020'
__credits__ = ['Chet Coenen']
__license__ = '/LICENSE'
__version__ = ''
__status__ = ''
#==============================================================================
# Contact
#==============================================================================
__maintainer__ = 'Chet Coenen'
__email__ = 'chet.m.coenen@icloud.com'
__socials__ = '@Denimbeard'
__username__ = 'Denimbeard'
# =============================================================================
# Class Data
# =============================================================================
__course__ = ''
__date__ = ''
__teammates__ = ['Chet Coenen']
__laboratory__ = ''
__description__ = ''
__studentid__ = '33683213'
# =============================================================================

def count(S, m, n):  
    if (n == 0): 
        return 1 
    if (n < 0): 
        return 0; 
    if (m <=0 and n >= 1): 
        return 0
    return count(S, m - 1, n) + count( S, m, n-S[m-1] );
    

arr = [1, 5, 12, 20] 
m = len(arr) 

print(count(arr, m, 16))

S = 16
coinList = [1, 5, 12, 20]
change = []
i = len(coinList)

def bettyCoin():
    while coinList[i] <= S:
        amend.change(coinList[i])
        S = S - coinList[i]
    return change


"""
This is broken and Im not sure why

def dynamic(n, m):
    for i from 0 to n+1:
        for j from 0 to m:

            if i equals 0:
                table[i, j] = 1

            else if j equals 0

            if i%S[j] equals 0
               table[i, j] = 1
        else 
               table[i, j] = 0;
    else if S[j] greater than i
         table[i, j] = table[i, j - 1]
    else 
         table[i, j] = table[i - S[j], j] + table[i, j-1]

  return table[n, m-1]
"""
