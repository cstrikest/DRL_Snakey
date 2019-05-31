#!/usr/bin/env python3

__author__ = "TheVoid"

from DRL_Snakey.agent import Agent
from DRL_Snakey.utils import DIRECTIONS

class StupidAgent(Agent):
	
	def visual_mode(self, Game, pos):
		return 0
	
	def button_K_e_pressed(self, Game):
		pass
	
	def get_next_direction(self, game):
		snake = game.main_snake
		x, y = snake.head_pos
		direction = snake.direction
		if direction == DIRECTIONS[1] and y == 19:
			return DIRECTIONS[3]
		elif direction == DIRECTIONS[3] and y == 19:
			return DIRECTIONS[0]
		elif direction == DIRECTIONS[0] and y == 0:
			return DIRECTIONS[3]
		elif direction == DIRECTIONS[3] and y == 0:
			return DIRECTIONS[1]
		else:
			return DIRECTIONS[1]
