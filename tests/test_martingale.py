"""
Description: Test class for BinBuilder
Author: Ross Logan 2017
"""
from unittest import TestCase
from roulette.martingale import Martingale
from roulette.outcome import Outcome
from roulette.bet import Bet
from roulette.table import Table

class TestMartingale(TestCase):

    def setUp(self):
        self.table = Table()
        self.martingale = Martingale(self.table)

    def testMartingaleCanPlaceBetsOnTable(self):
        bet = Bet(1.0, Outcome("BLACK", 1))
        self.martingale.placeBets()

        self.assertIn(bet, self.table.bets)

    def testMartingaleWin(self):
        bet = Bet(1.0, Outcome("BLACK", 1))

        self.martingale.placeBets()
        self.martingale.win(bet)

        winAmount = bet.winAmount() - self.martingale.stake
        self.assertEqual(0, self.martingale.lossCount)
        self.assertEqual(1, self.martingale.betMultiple)
        self.assertEqual(winAmount, self.martingale.stake)

    def testMartingaleLoss(self):
        bet = Bet(1.0, Outcome("BLACK", 1))

        self.martingale.placeBets()
        self.martingale.lose(bet)

        self.assertEqual(1, self.martingale.lossCount)
        self.assertEqual(2, self.martingale.betMultiple)