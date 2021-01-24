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
__description__ = 'Min-Max Algorithm'
__date__ = '1 December 2020 at 09:35'
#==============================================================================

def minmax(x):
    x = sorted(x)
    # Take your array and do an in place ascending sort
    
    l = len(x) - 1
    # Find the last item
    
    print("Min: {mi} :: Max: {ma}".format(mi=x[0], ma=x[l]))
    # Prints the first and last items, automatically giving the smallest and largest
