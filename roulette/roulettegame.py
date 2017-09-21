"""
Description:    Roulette Game class that manages the sequences of actions that defines a game of Roulette
Author:         Ross Logan 2017
"""

class RouletteGame(object):

    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table

    def cycle(self, player):
        if player.playing():
            player.placeBets()
            nextWinningBin = self.wheel.next()

            for bet in self.table.bets:
                if bet.outcome in nextWinningBin.outcomes:
                    player.win(bet)
                else:
                    player.lose(bet)

