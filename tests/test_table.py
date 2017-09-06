from unittest import TestCase
from roulette.table import Table
from roulette.bet import Bet
from roulette.outcome import Outcome
from exceptions.invalidbet import InvalidBetException

MISSING_BET_STRINGS_VALUE = "betStrings does not contain value, Iterator not working correctly?"


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

    def testBetsIterator(self):
        betFour = Bet(3, Outcome("test4", 2))
        betFive = Bet(2, Outcome("test5", 3))
        self.table.placeBet(self.betOne)
        self.table.placeBet(self.betTwo)
        self.table.placeBet(betFour)
        self.table.placeBet(betFive)

        betStrings = []
        for bet in self.table.bets:
            betStrings.append(str(bet))

        self.assertTrue("1 on test1" in betStrings, MISSING_BET_STRINGS_VALUE)
        self.assertTrue("2 on test2" in betStrings, MISSING_BET_STRINGS_VALUE)
        self.assertTrue("3 on test4" in betStrings, MISSING_BET_STRINGS_VALUE)
        self.assertTrue("2 on test5" in betStrings, MISSING_BET_STRINGS_VALUE)

    def testBetsToString(self):
        self.table.placeBet(self.betOne)
        self.table.placeBet(self.betTwo)

        self.assertEqual("1 on test1 2 on test2".strip(), self.table.__str__().strip())


