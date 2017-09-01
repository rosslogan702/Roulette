"""
Description: Test class for Bet
Author: Ross Logan 2017
"""

from unittest import TestCase
from roulette.bet import Bet
from roulette.outcome import Outcome

class TestBet(TestCase):

    def setUp(self):
        self.betOne = Bet(1, Outcome("test1", 1))
        self.betTwo = Bet(1, Outcome("test2", 3))
        self.betThree = Bet(1, Outcome("test3", 4))
        self.betFour = Bet(5, Outcome("test4", 4))

    def testWinAmount(self):
        self.assertEqual(2, self.betOne.winAmount())
        self.assertEqual(4, self.betTwo.winAmount())
        self.assertEqual(5, self.betThree.winAmount())
        self.assertEqual(25, self.betFour.winAmount())

    def testLoseAmount(self):
        self.assertEqual(1, self.betOne.loseAmount())
        self.assertEqual(1, self.betTwo.loseAmount())
        self.assertEqual(1, self.betThree.loseAmount())
        self.assertEqual(5, self.betFour.loseAmount())

    def testToString(self):
        self.assertEqual("5 on test4", self.betFour.__str__(), "String representation not as expected")
