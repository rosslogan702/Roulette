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

        self.assertEqual("00 (35:1)", str(self.wheel.get(37)), "Wheel does not have correct outcome added for zero"
                                                               " zero bet")

    def testGenerateNumberStraightBet(self):
        self.binBuilder.generateNumberStraightBet(self.wheel)

        for binIndex in range(1, 37):
            self.assertEqual(str(Outcome(str(binIndex), 35)), str(self.wheel.get(binIndex)),
                             "Wheel does not have correct outcome at index " + str(binIndex))

    def testGenerateStraightBets(self):
        self.binBuilder.generateStraightBets(self.wheel)

        self.assertEqual("0 (35:1)", str(self.wheel.get(0)),
                         "Wheel does not have correct outcome added for zero bet")
        self.assertEqual("00 (35:1)", str(self.wheel.get(37)),
                         "Wheel does not have correct outcome added for zero zero bet")

        for binIndex in range(1, 37):
            self.assertEqual(str(Outcome(str(binIndex), 35)), str(self.wheel.get(binIndex)),
                             "Wheel does not have correct outcome at index " + str(binIndex) + " zero bet")
