from unittest import TestCase
from roulette.table import Table
from roulette.bet import Bet
from roulette.outcome import Outcome
from exceptions.invalidbet import InvalidBetException

class TestTable(TestCase):

    def setUp(self):
        self.table = Table()
        self.betOne = Bet(1, Outcome("test1", 4))
        self.betTwo = Bet(2, Outcome("test2", 3))
        self.betThree = Bet(12, Outcome("test3", 4))

    def testIsValid(self):
        self.assertTrue(self.table.isValid(self.betOne))
        self.assertTrue(self.table.isValid(self.betTwo))
        self.assertFalse(self.table.isValid(self.betThree))

    def testPlaceBetValid(self):
        self.table.placeBet(self.betOne)
        self.table.placeBet(self.betTwo)

        self.assertIn(self.betOne, self.table.bets, "Bet one has not been added to table bets")
        self.assertIn(self.betTwo, self.table.bets, "Bet two has not been added to table bets")

    def testPlaceBetInvalid(self):
        self.assertRaises(InvalidBetException, lambda: self.table.placeBet(self.betThree))


