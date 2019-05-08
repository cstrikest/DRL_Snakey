#!/usr/bin/env python3

__author__ = "Yxzh"

import Snakey_core
import AI_core_logic

print("Start.")
G = Snakey_core.Snakey(bomb = 0)
i = 40
while True:
	G.next(AI_core_logic.get_next_direction(G.pos, G.food_pos, G.snakes))
	if G.deadflag:
		print("Game over. length:", G.ate + 2)
		G.reset()
		i -= 1
		if i is 0:
			break

