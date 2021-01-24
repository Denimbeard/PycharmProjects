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


# Player Attributes
class Human:
    cntdwn = 0

    def __init__(self, player, score, choice, script, start, cntdwn):
        """
        # Player Attribute
        :type player: str
        # Player Score
        :type score: int
        # Human Choice
        :type choice: str
        # Opening Script
        :type script: list[]
        # Variable starts the match:
        :type start: str
        #Timer:
        :type cntdwn: int

        """
        self.cntdwn = cntdwn
        self.player = player
        self.score = score
        self.choice = choice
        self.script = script
        self.start = start


# Computer Attributes
class Computer(Human):
    # Computer Choice
    pass


# TODO: Match Logic
class MatchLogic(Human, Computer):
    # Match Logic:

    # TODO: Rock Paper Scissor Rules:
    #  Rock beats scissor
    #  Paper beats rock
    #  Scissor beats paper

    # TODO:
    #  Player one decides on the count of three what option of the three they want to show
    #  Player two also decides, and they reveal at the same x

    # Timer (Seconds)
    while Human(player=str, score=int, script=list[str], choice=str, start='y', cntdwn=3):
        # define the countdown func
        while Human.cntdwn >= 0:
            print(time, end='... ')
            time.sleep(1)
            # Countdown from 3
            Human.cntdwn -= 1
        Human.Choice = input('SHOOT: (R/P/S): ')
    pass


# TODO: Reset Loop
class Reset(MatchLogic):
    # TODO:
    #  If not draw, show score for current session
    # TODO:
    #  If draw, immediately count down again
    pass


# TODO: Scoring
class Scoring(Human, Computer):
    # TODO: Output (p1) v (p2) = ?
    pass


# Variables:
x = Human('Player 1', 0, 'R',
          ['Rock Paper Scissor Rules:\n', 'Rock beats scissors\n', 'Paper beats rock\n',
           'Scissor beats paper\n', 'Player one decides on the count of three what option ',
           'of the three they want to show\n', 'Player two also decides, ', 'and they reveal at the same time\n'],
          input('Are you ready to play? y/n: '), 3)
y = Computer('Computer', 0, 'R', ' ', ' ', 1)
Computer.Choice = random.choice(['Rock', 'Paper', 'Scissors'])
