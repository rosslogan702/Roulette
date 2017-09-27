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
        self.martingale.setRounds(10)
        self.martingale.setStake(100)

    def testMartingaleCanPlaceBetsOnTable(self):
        bet = Bet(1.0, Outcome("BLACK", 1))
        self.martingale.placeBets()

        self.assertIn(bet, self.table.bets)

    def testMartingaleWin(self):
        bet = Bet(1.0, Outcome("BLACK", 1))
        initialStake = self.martingale.stake - bet.amount

        self.martingale.placeBets()
        self.martingale.win(bet)

        winAmount = bet.winAmount() + initialStake
        self.assertEqual(0, self.martingale.lossCount)
        self.assertEqual(1, self.martingale.betMultiple)
        self.assertEqual(winAmount, self.martingale.stake)

    def testMartingaleLoss(self):
        bet = Bet(1.0, Outcome("BLACK", 1))

        self.martingale.placeBets()
        self.martingale.lose(bet)

        self.assertEqual(1, self.martingale.lossCount)
        self.assertEqual(2, self.martingale.betMultiple)

    def testNoRoundsLeftPlaying(self):
        self.martingale.setRounds(0)
        self.assertFalse(self.martingale.checkRoundsToPlay())
        self.assertFalse(self.martingale.playing())

    def testRoundsLeftToPlay(self):
        self.martingale.setRounds(10)
        self.assertTrue(self.martingale.checkRoundsToPlay())
        self.assertTrue(self.martingale.playing())

    def testCheckCantBetPlayMoreThanStake(self):
        bet = Bet(1.0, Outcome("BLACK", 1))
        self.martingale.setStake(0)
        self.assertFalse(self.martingale.checkCanBetPlay(bet))

    def testCheckCantBetMoreThanTableLimit(self):
        bet = Bet(20.0, Outcome("BLACK", 1))
        self.assertFalse(self.martingale.checkCanBetPlay(bet))

    def testCheckCanBet(self):
        bet = Bet(4.0, Outcome("BLACK", 1))
        self.assertTrue(self.martingale.checkCanBetPlay(bet))

    def testCheckUserWantsToPlay(self):
        self.assertTrue(self.martingale.checkUserWantsToPlay())

    def testCheckUserDoesNotWantToPlay(self):
        self.assertFalse(self.martingale.checkUserWantsToPlay(False))
