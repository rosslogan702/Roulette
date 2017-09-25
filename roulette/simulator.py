"""
Description:    Simulator class that runs a number of cycles of the roulette game
Author:         Ross Logan 2017
"""

class Simulator(object):

    def __init__(self, game, player):
        self.initDuration = 1
        self.initStake = 100
        self.samples = 50
        self.durations = []
        self.maxima = []
        self.player = player
        self.game = game

    def session(self):
        self.player.setStake(self.initStake)
        self.player.setRounds(self.initDuration)
        stakeValues = []
        for cycles in range(0, self.initDuration):
            self.game.cycle(self.player)
            stakeValues.append(self.player.stake)
        return stakeValues




