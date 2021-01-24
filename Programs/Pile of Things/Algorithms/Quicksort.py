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
__description__ = 'Quick Sort Algorithm'
__date__ = '27 November 2020 at 19:39'
#==============================================================================

def sort(array):
# Here are your numbers to be sorted
    """Sort the array by using quicksort."""

    less = []
    # Less than the pivot

    equal = []
    # Equal to the pivot

    greater = []
    # Larger then the pivot

    if len(array) > 1:
    # If there are more than 1 thing in your array, do the following

        pivot = array[0]
        # Determines the pivot to be the first item in the array

        for x in array:
        # From here program goes through array one by one in order, left to right

            if x < pivot:
            # If the current item is less than the pivot, it is moved to less

                less.append(x)
                # Item was less

            elif x == pivot:
            # If the current item is equal to the pivot, it is moved to equal

                equal.append(x)
                # Item was equal

            elif x > pivot:
            # If the current item is greater than the pivot, it is moved to greater

                greater.append(x)
                # Item was greater

        # Don't forget to return something!
        return sort(greater)+equal+sort(less)
        # Just use the + operator to join lists

    # Note that you want equal ^^^^^ not pivot

    else:
    # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
