"""
Description: Wheel class that simulates a roulette wheel
Author: Ross Logan 2017
"""

from roulette.bin import Bin
from random import Random
from roulette.binbuilder import BinBuilder

class Wheel(object):

    def __init__(self, rng):
        self.bins = tuple(Bin() for i in range(38))
        self.rng = rng if rng is not None else Random.random()
        self.all_outcomes = {}

    def addOutcome(self, binIndex, outcome):
        self.all_outcomes[outcome.name] = outcome
        self.get(binIndex).add(outcome)

    def getOutcome(self, name):
        return self.all_outcomes[name]

    def next(self):
        return self.rng.choice(self.bins)

    def get(self, binIndex):
        return self.bins[binIndex]

def createWheel(rng):
    wheel = Wheel(rng)
    binBuilder = BinBuilder()
    binBuilder.buildBins(wheel)
    return wheel
