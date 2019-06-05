#!/usr/bin/env python3

__author__ = "Yxzh"

import random
from DRL_Snakey.utils import *
from DRL_Snakey.agent import Agent


class Logic(Agent):
	def elude(self, pos, snakes):  # 躲避
		l = list(DIRECTIONS)
		if predict_next_position(l[0], pos) not in snakes:
			temp = l[0]
		elif predict_next_position(l[1], pos) not in snakes:
			temp = l[1]
		elif predict_next_position(l[2], pos) not in snakes:
			temp = l[2]
		elif predict_next_position(l[3], pos) not in snakes:
			temp = l[3]
		else:
			temp = l[random.randrange(0, 4)]
		return temp
	
	def visual_mode(self, Game, pos):
		return 0
	
	def custom_function(self, Game):
		pass
	
	def get_next_direction(self, game):
		"""
		根据环境，通过决策算法返回前进的方向。这是决策类中必不可少的一个函数。
		:param game: 游戏
		:return: 决定的前进方向
		"""
		Hs = game.main_snake.head_pos[0] - game.food_pos[0]  # 横向差值
		Vs = game.main_snake.head_pos[1] - game.food_pos[1]  # 纵向差值
		
		if abs(Hs) > abs(Vs):
			if Hs < 0:
				temp = DIRECTIONS[3]
				if predict_next_position(temp, game.main_snake.head_pos) in game.main_snake.snakes:
					return self.elude(game.main_snake.head_pos, game.main_snake.snakes)[0]
			else:
				temp = DIRECTIONS[2]
				if predict_next_position(temp, game.main_snake.head_pos) in game.main_snake.snakes:
					return self.elude(game.main_snake.head_pos, game.main_snake.snakes)[0]
		else:
			if Vs < 0:
				temp = DIRECTIONS[1]
				if predict_next_position(temp, game.main_snake.head_pos) in game.main_snake.snakes:
					return self.elude(game.main_snake.head_pos, game.main_snake.snakes)[0]
			else:
				temp = DIRECTIONS[0]
				if predict_next_position(temp, game.main_snake.head_pos) in game.main_snake.snakes:
					return self.elude(game.main_snake.head_pos, game.main_snake.snakes)[0]
		return temp
