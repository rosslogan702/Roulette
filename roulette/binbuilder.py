"""
Description: BinBuilder class that builds the various permutations of outcomes in the bins on the wheel
Author: Ross Logan 2017
"""

from roulette.outcome import Outcome

class BinBuilder(object):
    def __init__(self):
        pass

    def buildBins(self, wheel):
        self.generateStraightBets(wheel)
        self.generateSplitBets(wheel)
        self.generateStreetBets(wheel)
        self.generateCornerBets(wheel)
        self.generateLineBets(wheel)
        self.generateDozenBets(wheel)
        self.generateColumnBets(wheel)
        self.generateEvenMoneyBets(wheel)

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

    def generateSplitBets(self, wheel):
        self.generateLeftRightPairsRows(wheel)
        self.generateUpDownPairsRows(wheel)

    def generateLeftRightPairsRows(self, wheel):
        for rowIndex in range(0, 12):
            wheel.addOutcome(rowIndex * 3 + 1, Outcome(str(rowIndex * 3 + 1) + "-" + str(rowIndex * 3 + 2), 17))
            wheel.addOutcome(rowIndex * 3 + 2, Outcome(str(rowIndex * 3 + 1) + "-" + str(rowIndex * 3 + 2), 17))
            wheel.addOutcome(rowIndex * 3 + 2, Outcome(str(rowIndex * 3 + 2) + "-" + str(rowIndex * 3 + 3), 17))
            wheel.addOutcome(rowIndex * 3 + 3, Outcome(str(rowIndex * 3 + 2) + "-" + str(rowIndex * 3 + 3), 17))

    def generateUpDownPairsRows(self, wheel):
        for num in range(1, 34):
            wheel.addOutcome(num, Outcome(str(num) + "-" + str(num + 3), 17))
            wheel.addOutcome(num + 3, Outcome(str(num) + "-" + str(num + 3), 17))

    def generateStreetBets(self, wheel):
        for rowIndex in range(0, 12):
            streetBetOutcome = self._generateStreetBetOutcome(rowIndex)
            for num in range(1, 4):
                wheel.addOutcome(rowIndex * 3 + num, streetBetOutcome)

    def _generateStreetBetOutcome(self, rowIndex):
        return Outcome(str(rowIndex * 3 + 1) + "-" + str(rowIndex * 3 + 2) + "-" + str(rowIndex * 3 + 3),
                       11)

    def generateCornerBets(self, wheel):
        for rowIndex in range(0, 11):
            colOneNum = rowIndex * 3 + 1
            colTwoNum = rowIndex * 3 + 2
            colOneOutcome = self._generateCornerBetOutcome(colOneNum)
            colTwoOutcome = self._generateCornerBetOutcome(colTwoNum)
            for colNum in range(0, 5):
                wheel.addOutcome(colOneNum + colNum, colOneOutcome)
                wheel.addOutcome(colTwoNum + colNum, colTwoOutcome)

    def _generateCornerBetOutcome(self, colOneNum):
        return Outcome(
            str(colOneNum) + "-" + str(colOneNum + 1) + "-" + str(colOneNum + 3) + "-" + str(colOneNum + 4), 8)

    def generateLineBets(self, wheel):
        for rowIndex in range(0, 11):
            colOneNum = rowIndex * 3 + 1
            lineOutcomeObject = self._generateLineOutcomeObject(colOneNum)
            for col in range(0, 6):
                wheel.addOutcome(colOneNum + col, lineOutcomeObject)

    def _generateLineOutcomeObject(self, colNum):
        return Outcome(str(colNum) + "-" + str(colNum + 1) + "-" + str(colNum + 2) + "-" +
                       str(colNum + 3) + "-" + str(colNum + 4) + "-" + str(colNum + 5), 5)

    def generateDozenBets(self, wheel):
        for dozen in range(0, 3):
            dozenOutcome = Outcome("Dozen-" + str(dozen+1), 2)
            for dozenNum in range(0, 12):
                wheel.addOutcome(12*dozen + dozenNum + 1, dozenOutcome)

    def generateColumnBets(self, wheel):
        for col in range(0, 3):
            colOutcome = Outcome("Col-" + str(col+1), 2)
            for row in range(0, 12):
                wheel.addOutcome(3*row + col + 1, colOutcome)

    def generateEvenMoneyBets(self, wheel):
        redOutcome = Outcome("RED", 1)
        blackOutcome = Outcome("BLACK", 1)
        evenOutcome = Outcome("EVEN", 1)
        oddOutcome = Outcome("ODD", 1)
        highOutcome = Outcome("HIGH", 1)
        lowOutcome = Outcome("LOW", 1)
        redNums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

        for num in range(1, 37):
            if num < 19:
                wheel.addOutcome(num, lowOutcome)
            if num > 19:
                wheel.addOutcome(num, highOutcome)
            if num%2 == 0:
                wheel.addOutcome(num, evenOutcome)
            if num%2 != 0:
                wheel.addOutcome(num, oddOutcome)
            if num in redNums:
                wheel.addOutcome(num, redOutcome)
            if num not in redNums:
                wheel.addOutcome(num, blackOutcome)
