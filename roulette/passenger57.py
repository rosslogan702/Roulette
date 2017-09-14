"""
Description:    Passenger 57 class that always bets on black, this will be replaced in future with Player class
                No Unit Testing will be added for this, as it is going to be replaced in the future
Author:         Ross Logan 2017
"""
from roulette.outcome import Outcome
from roulette.bet import Bet
from roulette.player import Player

class PassengerFiftySeven(Player):

    def __init__(self, table):
        self.black = Outcome("BLACK", 1)
        self.playerWon = False
        super().__init__(table)

    def placeBets(self):
        bet = Bet(2, self.black)
        self.table.placeBet(bet)
        self.stake -= bet.amount

    def win(self, bet):
        print("The following bet won: " + str(bet))
        self.playerWon = True
        self.stake += bet.winAmount()

    def lose(self, bet):
        print("The following bet lost: " + str(bet))
        self.playerWon = False

    def playerWon(self):
        return self.playerWon


