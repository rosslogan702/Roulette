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

    def playing(self):
        return True

    @abstractmethod
    def placeBets(self):
        pass

    def win(self, bet):
        pass

    def lose(self, bet):
        pass