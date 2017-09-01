"""
Description: Bet class that holds the amount bet and on which outcome
Author: Ross Logan 2017
"""

class Bet(object):

    def __init__(self, amount, outcome):
        self.amount = amount
        self.outcome = outcome

    def winAmount(self):
        return self.outcome.winAmount(self.amount) + self.amount

    def loseAmount(self):
        return self.amount


