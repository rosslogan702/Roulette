"""
Description: Subclass of abstract class player that implements martingale betting strategy
Author: Ross Logan 2017
"""

from roulette.player import Player
from math import pow


class Martingale(Player):

    def __init__(self):
        self.lossCount = 0
        self.betMultiple = pow(2, self.lossCount)

    def placeBets(self):
        pass

    def win(self, bet):
        pass

    def lose(self, bet):
        pass

