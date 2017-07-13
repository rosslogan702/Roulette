"""
Description: Class which contains a single outcome on which a bet can be placed
Author: Ross Logan 2017
"""


class Outcome(object):

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def winAmount(self, amount):
        return self.odds * amount

    def __eq__(self, outcome):
        return self.name == outcome.name

    def __ne__(self, outcome):
        return self.name != outcome.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return "%s (%d:1)" % (self.name, self.odds)

