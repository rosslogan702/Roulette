"""
Description: BinBuilder class that builds the various permutations of outcomes in the bins on the wheel
Author: Ross Logan 2017
"""

from roulette.outcome import Outcome

class BinBuilder(object):

    def __init__(self):
        pass

    def generateStraightBets(self, wheel):
        self.generateZeroStraightBet(wheel)
        self.generateZeroZeroStraightBet(wheel)
        self.generateNumberStraightBet(wheel)

    def generateZeroStraightBet(self, wheel):
        wheel.addOutcome(0, Outcome("0", 35))

    def generateZeroZeroStraightBet(self, wheel):
        wheel.addOutcome(37, Outcome("00", 35))

    def generateNumberStraightBet(self, wheel):
        for binIndex in range(1, 37):
            wheel.addOutcome(binIndex, Outcome(str(binIndex), 35))

    def generateLeftRightPairsFirstRow(self, wheel):
        wheel.addOutcome(1, Outcome("1-2", 17))
        wheel.addOutcome(2, Outcome("1-2", 17))
        wheel.addOutcome(2, Outcome("2-3", 17))
        wheel.addOutcome(3, Outcome("2-3", 17))

    def generateLeftRightPairsSecondRow(self, wheel):
        wheel.addOutcome(4, Outcome("4-5", 17))
        wheel.addOutcome(5, Outcome("4-5", 17))
        wheel.addOutcome(5, Outcome("5-6", 17))
        wheel.addOutcome(6, Outcome("5-6", 17))

    def generateLeftRightPairsRows(self, wheel):
        for rowIndex in range(0, 12):
            wheel.addOutcome(rowIndex*3 + 1, Outcome(str(rowIndex*3+1) + "-" + str(rowIndex*3+2), 17))
            wheel.addOutcome(rowIndex*3 + 2, Outcome(str(rowIndex*3+1) + "-" + str(rowIndex*3+2), 17))
            wheel.addOutcome(rowIndex*3 + 2, Outcome(str(rowIndex*3+2) + "-" + str(rowIndex*3+3), 17))
            wheel.addOutcome(rowIndex*3 + 3, Outcome(str(rowIndex*3+2) + "-" + str(rowIndex*3+3), 17))