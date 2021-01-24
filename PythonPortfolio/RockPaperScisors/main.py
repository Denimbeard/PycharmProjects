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
import random


class Start:
    print('Rock Paper Scissor Rules:\n', 'Rock beats scissors\n', 'Paper beats rock\n', 'Scissor beats paper\n',
          'Player one decides on the count of three what option of the three they want to show\n',
          'Player two also decides, and they reveal at the same time\n')
    start: str = input('Are you ready to play? y/n: ')


class Human:
    def __init__(self, player, score, choice):
        # Player
        self.player = player
        self.score = 0
        # Human Choice
        self.choice = 'R'


class Computer(Human):
    # Computer Choice
    pass


class MatchLogic(Human, Computer):
    # Match Logic:

    # Rock Paper Scissor Rules:
    # Rock beats scissor
    # Paper beats rock
    # Scissor beats paper

    # Player one decides on the count of three what option of the three they want to show
    # Player two also decides, and they reveal at the same x

    # Timer (Seconds)
    t = 3
    while start := 'y':
        # define the countdown func
        while t >= 0:
            print(t, end='... ')
            time.sleep(1)
            # Countdown from 3
            t -= 1
            Human.Choice = input('SHOOT: (R/P/S)')
            break
    pass

# Reset Loop
class Reset(MatchLogic):
    # If not draw, show score for current session
    # If draw, immediately count down again
    pass


# Scoring
class Scoring(Human, Computer):
    # Output (p1) v (p2) = ?
    # print('Player: ', shot, 'Computer: ', computer, ' || Score: ', scoreH, ' : ', scoreC)
    pass


x = Human('Player 1', 0, 'R')
y = Computer('Computer', 0, 'R')
Computer.Choice = random.choice(['Rock', 'Paper', 'Scissors'])