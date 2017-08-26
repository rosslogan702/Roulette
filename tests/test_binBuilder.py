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

    def testGenerateZeroStraightBet(self):
        self.binBuilder.generateZeroStraightBet(self.wheel)

        self.assertEqual("0 (35:1)", str(self.wheel.get(0)), "Wheel does not have correct outcome added for zero bet")

    def testGenerateZeroZeroStraightBet(self):
        self.binBuilder.generateZeroZeroStraightBet(self.wheel)

        self.assertEqual("00 (35:1)", str(self.wheel.get(37)),
                         "Wheel does not have correct outcome added for zero zero bet")

    def testGenerateNumberStraightBet(self):
        self.binBuilder.generateNumberStraightBet(self.wheel)

        for binIndex in range(1, 37):
            self.assertTrue(str(Outcome(str(binIndex), 35)) in str(self.wheel.get(binIndex)),
                             "Wheel does not have correct outcome at index " + str(binIndex))

    def testGenerateStraightBets(self):
        self.binBuilder.generateStraightBets(self.wheel)

        self.testGenerateZeroStraightBet()
        self.testGenerateZeroStraightBet()
        self.testGenerateNumberStraightBet()


    def testGenerateLeftRightPairs(self):
        self.binBuilder.generateLeftRightPairsRows(self.wheel)

        for rowIndex in range(0, 12):
            self.assertTrue(str(rowIndex * 3 + 1) + "-" + str(rowIndex * 3 + 2) + " (17:1)" in str(
                self.wheel.get(rowIndex * 3 + 1)),"Wheel does not have the correct outcomes for bin "
                + str(rowIndex * 3 + 1) + "left right split bets")
            self.assertTrue(str(rowIndex * 3 + 1) + "-" + str(rowIndex * 3 + 2) + " (17:1)" in str(
                self.wheel.get(rowIndex * 3 + 2)), "Wheel does not have the correct outcomes for bin " + str(
                rowIndex * 3 + 2) + " left right split bets")
            self.assertTrue(str(rowIndex * 3 + 2) + "-" + str(rowIndex * 3 + 3) + " (17:1)" in str(
                self.wheel.get(rowIndex * 3 + 2)), "Wheel does not have the correct outcomes for bin " + str(
                rowIndex * 3 + 2) + " left right split bets")
            self.assertTrue(str(rowIndex * 3 + 2) + "-" + str(rowIndex * 3 + 3) + " (17:1)" in str(
                self.wheel.get(rowIndex * 3 + 3)), "Wheel does not have the correct outcomes for bin " + str(
                rowIndex * 3 + 3) + " left right split bets")

    def testGenerateUpDownPairs(self):
        self.binBuilder.generateUpDownPairsRows(self.wheel)

        for num in range(1, 34):
            self.assertTrue(str(num) + "-" + str(num + 3) + " (17:1)" in str(self.wheel.get(num)),
                             "wheel does not have the correct outcomes for bin " + str(num) + "up and down split bets")
            self.assertTrue(str(num) + "-" + str(num + 3) + " (17:1)" in str(self.wheel.get(num+3)),
                             "wheel does not have the correct outcomes for bin " + str(num+3) + "up and down split bets")

    def testGenerateSplitBets(self):
        self.binBuilder.generateLeftRightPairsRows(self.wheel)
        self.binBuilder.generateUpDownPairsRows(self.wheel)

        self.testGenerateUpDownPairs()
        self.testGenerateLeftRightPairs()

    def testGenerateStreetBets(self):
        self.binBuilder.generateStreetBets(self.wheel)

        for rowIndex in range(0, 12):
            self.assertTrue(str(rowIndex*3+1) + "-" + str(rowIndex*3+2) + "-" + str(rowIndex*3+3) + " (11:1)" in
                            str(self.wheel.get(rowIndex*3+1)), "Wheel does not have the correct outcomes for bin "
                            + str(rowIndex*3+1) + " for street bets")
            self.assertTrue(str(rowIndex*3+1) + "-" + str(rowIndex*3+2) + "-" + str(rowIndex*3+3) + " (11:1)" in
                            str(self.wheel.get(rowIndex*3+2)), "Wheel does not have the correct outcomes for bin "
                            + str(rowIndex*3+2) + " for street bets")
            self.assertTrue(str(rowIndex*3+1) + "-" + str(rowIndex*3+2) + "-" + str(rowIndex*3+3) + " (11:1)" in
                            str(self.wheel.get(rowIndex*3+2)), "Wheel does not have the correct outcomes for bin "
                            + str(rowIndex*3+3) + " for street bets")




    #TODO: Once all the bets are completed, still need one test to cover all possible bets that tests everything




