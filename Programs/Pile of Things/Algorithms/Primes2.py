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

# Natural number generator
def nats(n):
    # Offers n
    yield n
    # Will continue to offer the next number
    yield from nats(n+1)
    return n

# Prime sieve
def sieve(s):
    n = next(s)
    yield n
    # get a number from the generator, offer a number that has no remainders
    yield from sieve( i for i in s if i%n!=0)
    return s

def rngprime():
    n = int(input('How many prime numbers do you want: '))
    print(sieve(range(n)))

