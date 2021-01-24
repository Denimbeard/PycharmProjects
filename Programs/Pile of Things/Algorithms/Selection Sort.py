#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# 
# =============================================================================
__author__ = 'Chet Coenen'
__copyright__ = 'Copyright 2020'
__credits__ = ['Chet Coenen']
__license__ = '/LICENSE'
__version__ = '1.0'
__maintainer__ = 'Chet Coenen'
__email__ = 'chet.m.coenen@icloud.com'
__socials__ = '@Denimbeard'
__status__ = 'Complete'
__description__ = 'Selection Sort Algorithm'
__date__ = '30 November 2020 at 13:05'
#==============================================================================

sortees = [-2, 45, 0, 11, -9]
# list of digits to sort

for position in range(len(sortees)):
    # starting from position 1 to position (length of sortees)

    smallestItem = min(sortees[position:])
    #find smallest element

    min_index = sortees[position:].index(smallestItem)
    #find position of smallest element

    sortees[position + min_index] = sortees[position]
    #replace element at min_index with first element

    sortees[position] = smallestItem
    #replace first element with min element

print(sortees)
