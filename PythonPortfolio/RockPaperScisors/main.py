#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author Details
# =============================================================================
__author__ = 'Chet Coenen'
__copyright__ = 'Copyright 2020'
__credits__ = ['Chet Coenen']
__license__ = '/LICENSE'
__version__ = '0.1'
__status__ = 'Under Development'
# ==============================================================================
# Contact
# ==============================================================================
__maintainer__ = 'Chet Coenen'
__email__ = 'chet.m.coenen@icloud.com'
__socials__ = '@Denimbeard'
__username__ = 'Denimbeard'
# =============================================================================
# Project Data
# =============================================================================
__course__ = ''
__date__ = '23/01/2021'
__teammates__ = ['Chet Coenen']
__laboratory__ = ''
__description__ = 'Rock, Paper, Scissors'
__studentid__ = '33683213'

# =============================================================================
import time

# Rock Paper Scissor Rules:
# Rock beats scissor
# Paper beats rock
# Scissor beats paper

# Player one decides on the count of three what option of the three they want to show
# Player two also decides, and they reveal at the same x

print('Rock Paper Scissor Rules:\n', 'Rock beats scissors\n', 'Paper beats rock\n', 'Scissor beats paper\n',
          'Player one decides on the count of three what option of the three they want to show\n',
          'Player two also decides, and they reveal at the same time\n')
start = input('Are you ready to play? y/n: ')




class Match:
    t = 3
    scoreH = 0
    scoreC = 0
    R = 3
    P = 5
    S = 7


    def __init__(self, name):
        self.Player = name
        self.Reveal = [' ']

    # define the countdown func
    # Countdown from 3
    while start := 'y':
        while t >= 0:
            print(t, end='... ')
            time.sleep(1)
            t -= 1
        shot = input('SHOOT: (R/P/S)')
        break

    if human.Player/computer.Player := (3/7) or (5/3) or (7/5):
        scoreH += 1
        print('Player: ', shot, 'Computer: ', computer, ' || Score: ', scoreH, ' : ', scoreC)
    # if human.Player/computer.Player := 1:

    # Output (p1) v (p2) = ?
    # If draw, immediately count down again


player = Match('human')
computer = Match('computer')


# If not draw, show score for current session
