#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
__author__ = 'Chet Coenen'
__copyright__ = 'Copyright 2020'
__credits__ = ['Chet Coenen']
__license__ = '/LICENSE'
__version__ = '0.1'
__maintainer__ = 'Chet Coenen'
__email__ = 'chet.m.coenen@icloud.com'
__status__ = 'Building'
__course__ = 'Foundations of Programing 2020'
__description__ = 'Term 1 Assignment'
__instructor__ = 'Max Garagnani'
__date__ = '4 December 18:00'
__filename__ = 'FSA_Python.py'
# ==============================================================================
# Variables
# ==============================================================================
# Each accepted digit
a = 'a'
b = 'b'
c = 'c'
i = 0
# Placement in attempted string

# Inputted array from the user
arr = input(str('Please enter the string to be recognized: '))

# testing
# arr = 'bbaccb'
# ==============================================================================
"""
In this recognizer, the starting state is S1, and S7 is the only accepting state
(empty strings are not accepted). Your program should ask the user to enter a
string and print "True" if the FSA accepts it, "False" otherwise. After printing
the result (and a 'Goodbye' message), the program should immediately stop.
"""

"""
Step 1:
    If arr[i] is an a, fail.
    If b, go to next step with next digit.
    If c, check digit 2
"""


def step1(fstate):
    global i
    # print(arr[i])
    if arr[i] == a:
        print(false())
    if arr[i] == b:
        forward(fstate)
        step2(fstate)
    if arr[i] == c:
        forward(fstate)
        step1(fstate)
    else:
        print(false())


"""
Step 2:
    If arr[i] is an a, return to step 1 with next digit.
    If b, go to next step with next digit.
    If c, fail.
"""


def step2(fstate):
    global i
    # print(arr[i])
    if arr[i] == a:
        forward(fstate)
        step1(fstate)
    if arr[i] == b:
        forward(fstate)
        step3(fstate)
    if arr[i] == c:
        print(false())
    else:
        print(false())


"""
Step 3:
    If arr[i] is an a, go to next step with next digit.
    If b, fail.
    If c, fail.
"""


def step3(fstate):
    global i
    # print(arr[i])
    if arr[i] == a:
        forward(fstate)
        step4(fstate)
    if arr[i] == b or c:
        print(false())
    else:
        print(false())


"""
Step 4:
    If arr[i] is an a, check the next digit.
    If b, return to step 3 with the next digit.
    If c, go to next step with next digit.
"""


def step4(fstate):
    global i
    # print(arr[i])
    if arr[i] == a:
        forward(fstate)
        step4(fstate)
    if arr[i] == b:
        forward(fstate)
        step3(fstate)
    if arr[i] == c:
        forward(fstate)
        step5(fstate)
    else:
        print(false())


"""
Step 5:
    If arr[i] is an a, fail.
    If b, return to step 3 with the next digit.
    If c, go to next step with next digit.
"""


def step5(fstate):
    global i
    # print(arr[i])
    if arr[i] == a:
        print(false())
    if arr[i] == b:
        forward(fstate)
        step3(fstate)
    if arr[i] == c:
        forward(fstate)
        step6(fstate)
    else:
        print(false())


"""
Step 6:
    If arr[i] is an a, return to step 5 with next digit.
    If b, complete task.
    If c, check next digit.
"""


def step6(fstate):
    global i
    # print(arr[i])
    if arr[i] == a:
        forward(fstate)
        step5(fstate)
    if arr[i] == b:
        print(true())
    if arr[i] == c:
        step6(fstate)
    else:
        print(false())


# If the program completes the task, then it's 'True'.
def true():
    # print(arr[i])
    print('True.')
    print('Goodbye.')
    quit()


# Otherwise, the arr is 'False'.
def false():
    # print(arr[i])
    print('False.')
    print('Goodbye.')
    quit()


# Move to next item in string
def forward(s):
    global i
    i = i + 1
    # return i


# ==============================================================================
# To Do
# ==============================================================================
print(step1(arr))
