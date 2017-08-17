"""
Description: Wheel class that simulates a roulette wheel
Author: Ross Logan 2017
"""

from roulette.bin import Bin

class Wheel(object):

    def __init__(self, rng):
        self.bins = tuple(Bin() for i in range(38))
        self.rng = rng

    def addOutcome(self, binIndex, outcome):
        self.get(binIndex).add(outcome)

    def next(self):
        return self.rng.choice(self.bins)

    def get(self, bin):
        return self.bins[bin]
