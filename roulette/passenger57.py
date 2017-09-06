"""
Description:    Passenger 57 class that always bets on black, this will be replaced in future with Player class
                No Unit Testing will be added for this, as it is going to be replaced in the future
Author:         Ross Logan 2017
"""
from roulette.outcome import Outcome
from roulette.bet import Bet

class PassengerFiftySeven(object):

    def __init__(self, table):
        self.table = table
        self.black = Outcome("BLACK", 1)

    def placeBets(self):
        bet = Bet(2, self.black)
        self.table.placeBet(bet)

    def win(self, bet):
        print("The following bet won: " + str(bet))

    def lose(self, bet):
        print("The following bet lost: " + str(bet))


