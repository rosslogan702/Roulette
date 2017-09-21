"""
Description: Subclass of abstract class player that implements martingale betting strategy
Author: Ross Logan 2017
"""

from roulette.player import Player
from roulette.bet import Bet
from roulette.outcome import Outcome
from math import pow


class Martingale(Player):

    def __init__(self, table):
        self.lossCount = 0
        self.betMultiple = pow(2, self.lossCount)
        self.playerWon = False
        super().__init__(table)

    def placeBets(self):
        bet = Bet(self.betMultiple, Outcome("BLACK", 1))
        self.table.placeBet(bet)
        self.stake -= bet.amount

    def win(self, bet):
        super().win(bet)
        self.lossCount = 0
        self.betMultiple = 1
        self.playerWon = True

    def lose(self, bet):
        super().lose(bet)
        self.lossCount +=1
        self.betMultiple *= 2
        self.playerWon = False

