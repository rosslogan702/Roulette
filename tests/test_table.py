from unittest import TestCase
from roulette.table import Table
from roulette.bet import Bet
from roulette.outcome import Outcome

class TestTable(TestCase):

    def setUp(self):
        pass

    def testIsValid(self):
        # To test this, what we need to do is start of with an empty table
        # Place a few bets which should be accepted and below the table limit
        # Then loop through and place a bet which would bring the table over the limit
        # at this point ensure that the bet is refused and returned as not valid

        # Assumption, that is being made here is that the process of "adding" up all the bets
        # is totalling the win amounts possible from each bet and then using that figure as the
        # threshold to decide whether or not a bet is able to be placed

        table = Table()
        betOne = Bet(1, Outcome("test1", 4))
        print(betOne.winAmount())
        betTwo = Bet(2, Outcome("test2", 3))
        print(betTwo.winAmount())
        betThree = Bet(4, Outcome("test3", 5))
        print(betThree.winAmount())


