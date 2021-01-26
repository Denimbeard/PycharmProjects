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


    # Computer attributes
class Computer(Human):
    # Computer Choice
    pass


class MatchLogic(Human, Computer):
# TODO: Rock Paper Scissor Rules:
#  Rock beats scissor
#  Paper beats rock
#  Scissor beats paper

# TODO:
#  Player one decides on the count of three what option of the three they want to show
#  Player two also decides, and they reveal at the same x

# Timer (Seconds)

class Reset(MatchLogic):
    # TODO: If not draw, show score for current session
    # TODO: If draw, immediately count down again


class Scoring(Human, Computer):
    # TODO: Output (p1) v (p2) = ?
    pass


# Variables:
count = 3
shoot = 'SHOOT: (R/P/S)\n'
startScript: list[str]= ['Rock Paper Scissor Rules: ', 'Rock beats scissors', 'Paper beats rock',
              'Scissor beats paper', 'Player one decides on the count of three what option ',
              'of the three they want to show', 'Player two also decides, ', 'and they reveal at the same time']
print(startScript)
ready = input('Are you ready to play? y/n: ')



p1 = Human('Player 1', 0, 'R', startScript, ready, count)
p2 = Computer('Computer', 0, 'R', ' ', ' ', 1)
gameStart = False

Computer.Choice = random.choice(['Rock', 'Paper', 'Scissors'])

while ready:= 'y':
    gameStart = True

while gameStart:
        while count > 0:
            for i in range(count):
                print(str(count-i) + "...")
                time.sleep(1)
                print(shoot)






















