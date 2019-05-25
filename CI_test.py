#!/usr/bin/env python3

__author__ = "Yxzh"

import DRL_Snakey as Snakey


game = Snakey.Game(0)
agent = Snakey.agent.DP(iteration = 10, walk_reward = -0.8)
while not game.deathflag:
	game.next(agent.get_next_direction(game))
game.reset()
agent = Snakey.agent.Logic()
while not game.deathflag:
	game.next(agent.get_next_direction(game))
