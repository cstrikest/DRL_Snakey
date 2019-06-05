#!/usr/bin/env python3

__author__ = "Yxzh"

import DRL_Snakey as Snakey

def test(agent):
	while not game.deathflag:
		game.next_step(agent.get_next_direction(game))
	game.reset()
game = Snakey.Game(0)
test(Snakey.agent.Logic())
test(Snakey.agent.DP(iteration = 3, walk_reward = -0.8))
test(Snakey.agent.MC(iteration = 3, max_step = 3))
