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
# ==============================================================================
# Contact
# ==============================================================================
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
import sys

"""
Problem:
Given a[n] return the smallest integer >0 that does not occur in array
Ex: a = [1, 3, 6, 4, 1, 2]
    Returns: 5
Ex: a = [1, 2, 3]
    Returns: 4
    
n can be anything from 1 to 100,000 integers
a[n] can hold numbers from -1,000,000 to 1,000,000

"""
# Input user string
input_string = list(map(int, input("Enter a list elements separated by space ").split()))

def nextInteger(user_list):
    """

    """
    # Min value of item
    if any(x < -1000000 for x in user_list):
        raise Exception('Items exceeds the minimum integer size of -1,000,000.')
        sys.exit()
    # Max value of item
    if any(x > 1000000 for x in user_list):
        raise Exception('Items exceeds the maximum integer size of 1,000,000.')
        sys.exit()
    # User string must be between i = 1 =< 100,000
    if len(user_list) > 100000:
        raise Exception('Items exceeds the maximum allowed length of 100,000.')
        sys.exit()
    # If all digits of a[n] are negative, return 1
    if all(x < 0 for x in user_list):
        return 1
        sys.exit()

print(nextInteger(input_string))






