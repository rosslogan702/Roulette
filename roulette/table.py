"""
Description: Table class for holding bets
Author: Ross Logan 2017
"""
from exceptions.invalidbet import InvalidBetException

class Table(object):

    def __init__(self):
        self.limit = 10
        self.bets = []

    def isValid(self, bet):
        totalBetOnTable = 0
        for bet in self.bets:
            totalBetOnTable += bet.amount
        if totalBetOnTable + bet.amount <= self.limit:
            return True
        return False

    def placeBet(self, bet):
        if self.isValid(bet):
            self.bets.append(bet)
        else:
            raise InvalidBetException()

    def __iter__(self):
        self._it = iter(self.bets)
        return self

    def __next__(self):
        return next(self._it)

    def __str__(self):
        bets = ""
        for bet in self.bets:
            bets += str(bet) + " "
        return bets
