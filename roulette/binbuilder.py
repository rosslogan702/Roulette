"""
Description: BinBuilder class that builds the various permutations of outcomes in the bins on the wheel
Author: Ross Logan 2017
"""

from roulette.outcome import Outcome

#TODO: Refactor to remove the duplication of the code and in the test bin builder class
#TODO: Couple of remaining bin algorithms still to be implemented: Dozen bets, column bets & even money
#TODO: Add on CI every time there is a check in

class BinBuilder(object):

    def __init__(self):
        pass

    def generateStraightBets(self, wheel):
        self.generateZeroStraightBet(wheel)
        self.generateZeroZeroStraightBet(wheel)
        self.generateNumberStraightBet(wheel)

    def generateSplitBets(self, wheel):
        self.generateLeftRightPairsRows(wheel)
        self.generateUpDownPairsRows(wheel)

    def generateZeroStraightBet(self, wheel):
        wheel.addOutcome(0, Outcome("0", 35))

    def generateZeroZeroStraightBet(self, wheel):
        wheel.addOutcome(37, Outcome("00", 35))

    def generateNumberStraightBet(self, wheel):
        for binIndex in range(1, 37):
            wheel.addOutcome(binIndex, Outcome(str(binIndex), 35))

    def generateLeftRightPairsRows(self, wheel):
        for rowIndex in range(0, 12):
            wheel.addOutcome(rowIndex*3 + 1, Outcome(str(rowIndex*3+1) + "-" + str(rowIndex*3+2), 17))
            wheel.addOutcome(rowIndex*3 + 2, Outcome(str(rowIndex*3+1) + "-" + str(rowIndex*3+2), 17))
            wheel.addOutcome(rowIndex*3 + 2, Outcome(str(rowIndex*3+2) + "-" + str(rowIndex*3+3), 17))
            wheel.addOutcome(rowIndex*3 + 3, Outcome(str(rowIndex*3+2) + "-" + str(rowIndex*3+3), 17))

    def generateUpDownPairsRows(self, wheel):
        for num in range(1, 34):
            wheel.addOutcome(num, Outcome(str(num) + "-" + str(num+3), 17))
            wheel.addOutcome(num+3, Outcome(str(num) + "-" + str(num+3), 17))

    #TODO: Could probably simplify this code further with loop around the add outcome
    def generateStreetBets(self, wheel):
        for rowIndex in range(0, 12):
            wheel.addOutcome(rowIndex * 3 + 1,
                             self._generateStreetBetOutcome(rowIndex))
            wheel.addOutcome(rowIndex * 3 + 2,
                             self._generateStreetBetOutcome(rowIndex))
            wheel.addOutcome(rowIndex * 3 + 3,
                             self._generateStreetBetOutcome(rowIndex))

    def _generateStreetBetOutcome(self, rowIndex):
        return Outcome(str(rowIndex * 3 + 1) + "-" + str(rowIndex * 3 + 2) + "-" + str(rowIndex * 3 + 3),
                       11)

    def generateCornerBets(self, wheel):
        for rowIndex in range(0, 11):
            colOneNum = rowIndex * 3 + 1
            colTwoNum = rowIndex * 3 + 2

            wheel.addOutcome(colOneNum, Outcome(
                str(colOneNum) + "-" + str(colOneNum + 1) + "-" + str(colOneNum + 3) + "-" + str(colOneNum + 4), 8))
            wheel.addOutcome(colOneNum + 1, Outcome(
                str(colOneNum) + "-" + str(colOneNum + 1) + "-" + str(colOneNum + 3) + "-" + str(colOneNum + 4), 8))
            wheel.addOutcome(colOneNum + 3, Outcome(
                str(colOneNum) + "-" + str(colOneNum + 1) + "-" + str(colOneNum + 3) + "-" + str(colOneNum + 4), 8))
            wheel.addOutcome(colOneNum + 4, Outcome(
                str(colOneNum) + "-" + str(colOneNum + 1) + "-" + str(colOneNum + 3) + "-" + str(colOneNum + 4), 8))

            wheel.addOutcome(colTwoNum, Outcome(
                str(colTwoNum) + "-" + str(colTwoNum + 1) + "-" + str(colTwoNum + 3) + "-" + str(colTwoNum + 4), 8))
            wheel.addOutcome(colTwoNum + 1, Outcome(
                str(colTwoNum) + "-" + str(colTwoNum + 1) + "-" + str(colTwoNum + 3) + "-" + str(colTwoNum + 4), 8))
            wheel.addOutcome(colTwoNum + 3, Outcome(
                str(colTwoNum) + "-" + str(colTwoNum + 1) + "-" + str(colTwoNum + 3) + "-" + str(colTwoNum + 4), 8))
            wheel.addOutcome(colTwoNum + 4, Outcome(
                str(colTwoNum) + "-" + str(colTwoNum + 1) + "-" + str(colTwoNum + 3) + "-" + str(colTwoNum + 4), 8))

    def generateLineBets(self, wheel):
        for rowIndex in range(0, 11):
            colOneNum = rowIndex * 3 + 1
            wheel.addOutcome(colOneNum,
                             self._generateLineOutcomeObject(colOneNum))
            wheel.addOutcome(colOneNum + 1,
                             self._generateLineOutcomeObject(colOneNum))
            wheel.addOutcome(colOneNum + 2,
                             self._generateLineOutcomeObject(colOneNum))
            wheel.addOutcome(colOneNum + 3,
                             self._generateLineOutcomeObject(colOneNum))
            wheel.addOutcome(colOneNum + 4,
                             self._generateLineOutcomeObject(colOneNum))
            wheel.addOutcome(colOneNum + 5,
                             self._generateLineOutcomeObject(colOneNum))

    def _generateLineOutcomeObject(self, colNum):
        return Outcome(str(colNum) + "-" + str(colNum + 1) + "-" + str(colNum + 2) + "-" +
                       str(colNum + 3) + "-" + str(colNum + 4) + "-" + str(colNum + 5), 5)
