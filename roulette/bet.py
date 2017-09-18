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

    def __str__(self):
        return str(self.amount) + " on " + self.outcome.name

    def __eq__(self, bet):
         if self.amount == bet.amount and self.outcome.__eq__(bet.outcome):
             return True
         return False

    def __ne__(self, bet):
        if self.amount != bet.amount or self.out.__ne__(bet.outcome):
            return True
        return False

    def __hash__(self) -> int:
        return super().__hash__()



