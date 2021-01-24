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
__description__ = 'et of code to convert a whole number from base 10 to variable base without directly using base conversions'
__date__ = '30 November 2020 at 15:42'
#==============================================================================


n = int(input("Input a whole number to convert from base 10: "))
#User inputs a whole positive number, converted to an int

b = int(input("Input a base to convert into: "))
#User inputs the new base for their number, converted to an int

def toDigits(n, b):
    #Convert a positive number n to its digit representation in base b.
    
    digits = []
    #Digits is an empty array that will fill with the math
    
    while n > 0:
        #While your whole number is greater than 0 do the following
        
        digits.insert(0, n % b)
        #Insert into position 0 of digits array the remainder of n/b
        
        n  = n // b
        #Your whole number now equals the previous whole number divided by b, rounded down
        
    return digits
    #Print the array named digits
    
list = toDigits(n, b)
#Sets the resulting array to the variable list

def convert(list):
    #Converts the array into a single number
    
    res = int("".join(map(str, list)))
    return res
cr = convert(list)
print("The number {n} converted to base {b} is: {cr}." .format(n=n, b=b, cr=cr))
#Gives results
