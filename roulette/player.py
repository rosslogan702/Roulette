"""
Description:    Abstract class for Player
Author:         Ross Logan 2017
"""

from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, table):
        self.stake = 0
        self.roundsToGo = 0
        self.table = table
        self.stillPlaying = True
        self.playerWon = False

    def playing(self):
        return self.stillPlaying

    @abstractmethod
    def placeBets(self):
        pass

    def win(self, bet):
        self.stake += bet.winAmount()

    def lose(self, bet):
        pass