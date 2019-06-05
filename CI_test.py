#!/usr/bin/env python3

__author__ = "Yxzh"

import DRL_Snakey as Snakey

def test(agent, game):
	while not game.deathflag:
		game.next_step(agent.get_next_direction(game))
		print(game.main_snake.snakes)
	print(game.ate)
	game.reset()

game = Snakey.Game()
test(Snakey.agent.Logic(), game)
test(Snakey.agent.DP(iteration = 30, walk_reward = -0.8), game)
test(Snakey.agent.MC(iteration = 30, max_step = 300), game)
