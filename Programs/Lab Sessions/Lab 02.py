#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author Details
# =============================================================================
__author__ = 'Chet Coenen'
__copyright__ = 'Copyright 2020'
__credits__ = ['Chet Coenen']
__license__ = '/LICENSE'
__version__ = '1.0'
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
__course__ = 'Foundations of Programing'
__date__ = '8 December 2020'
__teammates__ = ['Chet Coenen']
__laboratory__ = ''
__description__ = 'Lab 2 Session Sheet'
# =============================================================================
# Instructions
#==============================================================================
"""
    Write a program that takes in input from the user the number of hours
    worked per week, the hourly pay, and the tax rate (as a number between
    0 and 1), and outputs the weekly gross and net pay rates.
"""
#==============================================================================
# Variables
#==============================================================================
# Hours worked
# Please enter the number of hours worked:
hours = float(input('Please enter the number of hours worked: '))
# Hourly Rate
# Please enter the hourly pay rate (in GBP per hour):
rate = float(input('Please enter the hourly pay rate (in GBP per hour): '))
# Tax Rate
# Please enter your tax rate:
tax = float(input('Please enter your tax rate (as a number between 0 and 1): '))
print('\n')
#==============================================================================
# Processes
#==============================================================================
#Weekly Gross Pay and Net Pay
gross = hours * rate
# Net Pay = Gross Pay * (1 - Tax Rate)
net = gross*(1-tax)
#==============================================================================
# Output
#==============================================================================
# Net Pay (in GBP):
print('Net Pay (in GBP): ', net)
# Gross Pay (in GBP):
print('Gross Pay (in GBP): ', gross)
# Rounded Results:
# Net Pay (in GBP):
print(f'Rounded Net Pay (in GBP): {net:.2f}')
# Gross Pay (in GBP):
print(f'Rounded Gross Pay (in GBP): {gross:.2f}')
