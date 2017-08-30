"""
Description: Test class for BinBuilder
Author: Ross Logan 2017
"""

from unittest import TestCase
from roulette.outcome import Outcome
from roulette.binbuilder import BinBuilder
from roulette.wheel import Wheel
from random import randint


class TestBinBuilder(TestCase):
    def setUp(self):
        randomNumberGenerator = randint
        self.wheel = Wheel(randomNumberGenerator)
        self.binBuilder = BinBuilder()
        self.redOutcome = Outcome("RED", 1)
        self.blackOutcome = Outcome("BLACK", 1)
        self.evenOutcome = Outcome("EVEN", 1)
        self.oddOutcome = Outcome("ODD", 1)
        self.highOutcome = Outcome("HIGH", 1)
        self.lowOutcome = Outcome("LOW", 1)
        self.redNums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    def testBuildBins(self):
        self.binBuilder.buildBins(self.wheel)

        self._checkAllBets(self.wheel)

    def _checkAllBets(self, wheel):
        self._checkStraightBets(wheel)
        self._checkSplitBets(wheel)
        self._checkStreetBets(wheel)
        self._checkCornerBets(wheel)
        self._checkLineBets(wheel)
        self._checkDozenBets(wheel)
        self._checkColumnBets(wheel)
        self._checkEvenMoneyBets(wheel, self.blackOutcome, self.evenOutcome, self.highOutcome, self.lowOutcome,
                                 self.oddOutcome, self.redNums, self.redOutcome)

    def testGenerateZeroStraightBet(self):
        self.binBuilder.generateZeroStraightBet(self.wheel)

        self._checkZeroStraightBet(self.wheel)

    def _checkZeroStraightBet(self, wheel):
        self.assertTrue("0 (35:1)" in str(wheel.get(0)), "Wheel does not have correct outcome added for zero bet")

    def testGenerateZeroZeroStraightBet(self):
        self.binBuilder.generateZeroZeroStraightBet(self.wheel)

        self._checkZeroZeroStraightBet(self.wheel)

    def _checkZeroZeroStraightBet(self, wheel):
        self.assertTrue("00 (35:1)" in str(wheel.get(37)),
                        "Wheel does not have correct outcome added for zero zero bet")

    def testGenerateNumberStraightBet(self):
        self.binBuilder.generateNumberStraightBet(self.wheel)

        self._checkNumberStraightBets(self.wheel)

    def _checkNumberStraightBets(self, wheel):
        for binIndex in range(1, 37):
            self.assertTrue(str(Outcome(str(binIndex), 35)) in str(wheel.get(binIndex)),
                            "Wheel does not have correct outcome at index " + str(binIndex))

    def testGenerateStraightBets(self):
        self.binBuilder.generateStraightBets(self.wheel)

        self._checkStraightBets(self.wheel)

    def _checkStraightBets(self, wheel):
        self._checkZeroStraightBet(wheel)
        self._checkZeroZeroStraightBet(wheel)
        self._checkNumberStraightBets(wheel)

    def testGenerateLeftRightPairs(self):
        self.binBuilder.generateLeftRightPairsRows(self.wheel)

        self._checkLeftRightPairs(self.wheel)

    def _checkLeftRightPairs(self, wheel):
        for rowIndex in range(0, 12):
            firstColOutcome = self._generateLeftRightOutcome(rowIndex, 1, 2)
            secondColOutcome = self._generateLeftRightOutcome(rowIndex, 2, 3)
            self.assertTrue(firstColOutcome in str(
                wheel.get(rowIndex * 3 + 1)), "Wheel does not have the correct outcomes for bin "
                            + str(rowIndex * 3 + 1) + "left right split bets")
            self.assertTrue(firstColOutcome in str(
                wheel.get(rowIndex * 3 + 2)), "Wheel does not have the correct outcomes for bin " + str(
                rowIndex * 3 + 2) + " left right split bets")
            self.assertTrue(secondColOutcome in str(
                wheel.get(rowIndex * 3 + 2)), "Wheel does not have the correct outcomes for bin " + str(
                rowIndex * 3 + 2) + " left right split bets")
            self.assertTrue(secondColOutcome in str(
                wheel.get(rowIndex * 3 + 3)), "Wheel does not have the correct outcomes for bin " + str(
                rowIndex * 3 + 3) + " left right split bets")

    def _generateLeftRightOutcome(self, rowIndex, leftCol, rightCol):
        return str(rowIndex * 3 + leftCol) + "-" + str(rowIndex * 3 + rightCol) + " (17:1)"

    def testGenerateUpDownPairs(self):
        self.binBuilder.generateUpDownPairsRows(self.wheel)

        self._checkUpDownPairs(self.wheel)

    def _checkUpDownPairs(self, wheel):
        for num in range(1, 34):
            self.assertTrue(str(num) + "-" + str(num + 3) + " (17:1)" in str(wheel.get(num)),
                            "wheel does not have the correct outcomes for bin " + str(num) + "up and down split bets")
            self.assertTrue(str(num) + "-" + str(num + 3) + " (17:1)" in str(wheel.get(num + 3)),
                            "wheel does not have the correct outcomes for bin " + str(
                                num + 3) + "up and down split bets")

    def testGenerateSplitBets(self):
        self.binBuilder.generateSplitBets(self.wheel)

        self._checkSplitBets(self.wheel)

    def _checkSplitBets(self, wheel):
        self._checkLeftRightPairs(wheel)
        self._checkUpDownPairs(wheel)

    def testGenerateStreetBets(self):
        self.binBuilder.generateStreetBets(self.wheel)

        self._checkStreetBets(self.wheel)

    def _checkStreetBets(self, wheel):
        for rowIndex in range(0, 12):
            streetBetOutcome = self._generateStreetBetOutcome(rowIndex)
            for num in range(1, 4):
                self.assertTrue(streetBetOutcome in
                                str(wheel.get(rowIndex * 3 + num)),
                                "Wheel does not have the correct outcomes for bin "
                                + str(rowIndex * 3 + num) + " for street bets")

    def _generateStreetBetOutcome(self, rowIndex):
        return str(rowIndex * 3 + 1) + "-" + str(rowIndex * 3 + 2) + "-" + str(rowIndex * 3 + 3) + " (11:1)"

    def testGenerateCornerBets(self):
        self.binBuilder.generateCornerBets(self.wheel)

        self._checkCornerBets(self.wheel)

    def _checkCornerBets(self, wheel):
        for rowIndex in range(0, 11):
            indexes = [rowIndex * 3 + 1, rowIndex * 3 + 2]
            for num in indexes:
                cornerBetOutcome = self._generateCornerBetOutcome(num)
                self.assertTrue(cornerBetOutcome in str(
                    wheel.get(num)),
                                "Wheel does not have the correct outcomes for bin " + str(num) + " for street bets")
                self.assertTrue(cornerBetOutcome in str(
                    wheel.get(num + 1)),
                                "Wheel does not have the correct outcomes for bin " + str(num + 1) + " for street bets")
                self.assertTrue(cornerBetOutcome in str(
                    wheel.get(num + 3)),
                                "Wheel does not have the correct outcomes for bin " + str(num + 3) + " for street bets")
                self.assertTrue(cornerBetOutcome in str(
                    wheel.get(num + 4)),
                                "Wheel does not have the correct outcomes for bin " + str(num + 4) + " for street bets")

    def _generateCornerBetOutcome(self, num):
        return str(num) + "-" + str(num + 1) + "-" + str(num + 3) + "-" + str(num + 4) + " (8:1)"

    def testGenerateLineBets(self):
        self.binBuilder.generateLineBets(self.wheel)

        self._checkLineBets(self.wheel)

    def _checkLineBets(self, wheel):
        for rowIndex in range(0, 11):
            colOneNum = rowIndex * 3 + 1

            for linenum in range(colOneNum, colOneNum + 6):
                self.assertTrue(str(colOneNum) + "-" + str(colOneNum + 1) + "-" + str(colOneNum + 2) + "-" +
                                str(colOneNum + 3) + "-" + str(colOneNum + 4) + "-" + str(colOneNum + 5) + " (5:1)" in
                                str(wheel.get(linenum)), "Wheel does not have the correct outcome for bin " +
                                str(linenum) + " for line bets")

    def testGenerateDozenBet(self):
        self.binBuilder.generateDozenBets(self.wheel)

        self._checkDozenBets(self.wheel)

    def _checkDozenBets(self, wheel):
        for d in range(0, 3):
            for num in range(0, 12):
                self.assertTrue("Dozen-" + str(d + 1) + " (2:1)" in str(wheel.get(12 * d + num + 1)))

    def testGenerateColumnBets(self):
        self.binBuilder.generateColumnBets(self.wheel)

        self._checkColumnBets(self.wheel)

    def _checkColumnBets(self, wheel):
        for col in range(0, 3):
            for row in range(0, 12):
                self.assertTrue("Col-" + str(col + 1) + " (2:1)" in str(wheel.get(3 * row + col + 1)))

    def testGenerateEvenMoneyBets(self):
        self.binBuilder.generateEvenMoneyBets(self.wheel)

        self._checkEvenMoneyBets(self.wheel, self.blackOutcome, self.evenOutcome, self.highOutcome, self.lowOutcome,
                                 self.oddOutcome, self.redNums, self.redOutcome)

    def _checkEvenMoneyBets(self, wheel, blackOutcome, evenOutcome, highOutcome, lowOutcome, oddOutcome, redNums,
                            redOutcome):
        for num in range(1, 37):
            if num < 19:
                self.assertTrue(str(lowOutcome) in str(wheel.get(num)))
            if num > 19:
                self.assertTrue(str(highOutcome) in str(wheel.get(num)))
            if num % 2 == 0:
                self.assertTrue(str(evenOutcome) in str(wheel.get(num)))
            if num % 2 != 0:
                self.assertTrue(str(oddOutcome) in str(wheel.get(num)))
            if num in redNums:
                self.assertTrue(str(redOutcome) in str(wheel.get(num)))
            if num not in redNums:
                self.assertTrue(str(blackOutcome) in str(wheel.get(num)))
