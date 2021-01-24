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
__description__ = 'Merge Sort Algorithm'
__date__ = '30 November 2020 at 15:42'
#==============================================================================
def mergesort(x):
    print('array: ', x)
    if len(x) < 2:
        print(x)
        return x
    # Check for digit in array
        
    sortedList = []
    # Empty list for results
    
    mid = int(len(x) / 2)
    # Finds mid of array provided, until finding a single sortable element
    
    firstItem = mergesort(x[:mid])
    # First item to compare
    
    secondItem = mergesort(x[mid:])
    # Second item to compare
    
    i = 0
    # Placement counter
    
    j = 0
    # Placement counter
    
    while i < len(firstItem) and j < len(secondItem):
    # While the length of compared lists are 0 do:
        
        if firstItem[i] > secondItem[j]:
        # If the first item of the first list is larger than the
        # first item of the second list then:
            print(sortedList)
            sortedList.append(secondItem[j])
            # Tack on the second item to the sorted list
            
            j += 1
            # Increase placement counter for first list
            print(sortedList)
        else:
            print(sortedList)
            sortedList.append(firstItem[i])
            # Tack on the first item to the sorted list
            
            i += 1
            # Increase placement counter for second list
            print(sortedList)
    sortedList += firstItem[i:]
    # Sorted list gains items
    print(sortedList)
    sortedList += secondItem[j:]
    # Sorted list gains items
    print(sortedList)
    return sortedList
    print(sortedList)
print(mergesort([95,25,55,18,12,65,86,20,8,45,9]))
