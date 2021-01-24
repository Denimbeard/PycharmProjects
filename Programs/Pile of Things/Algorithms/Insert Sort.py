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
__description__ = 'Insert Sort Algorithm'
__date__ = '30 November 2020 at 10:56'
#==============================================================================

lineup = [-2, 45, 0, 11, -9]
# digits to sort

def insert_sort(sortees):
# sortees is list to be sorted

    for position in range(1, len(sortees)):
        #starting from position 1 to position (length of sortees)

        defendant = sortees[position]
        # defendant selection

        judge = position - 1
        # judging will always be done by figure before defendant

        while (judge >= 0) and (sortees[judge] > defendant):
        # while the judges position is larger then 0 and the judge is larger then the defendant do this:

            sortees[judge+1] = sortees[judge]
            # move the judge over one place in the lineup

            judge = judge - 1
            # lower the postion count to get a new judge

        sortees[judge+1] = defendant
        #we now judge the next digit

insert_sort(lineup)
# sort the lineup

print(lineup)
# see results
