"""
Description: Test class for BinBuilder
Author: Ross Logan 2017
"""

from unittest import TestCase
from roulette.outcome import Outcome
from roulette.BinBuilder import BinBuilder
from roulette.wheel import Wheel
from random import randint

class TestBinBuilder(TestCase):

    def setUp(self):
        pass


    def testBuildBins(self):
        pass

    def testGenerateStraightBets(self):
        outcomeZero = Outcome("0", 35)
        outcomeZeroZero = Outcome("00", 35)
        randomNumberGenerator = randint
        wheel = Wheel(randomNumberGenerator)
        binBuilder = BinBuilder

        binBuilder.generateStraightBets(wheel)

        self.assertEqual(wheel.get(0))






