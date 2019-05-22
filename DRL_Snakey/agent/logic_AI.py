#!/usr/bin/env python3

__author__ = "Yxzh"

import random
from DRL_Snakey.agent import Agent


class Logic(Agent):
	@staticmethod
	def next(direction, pos):  # 预测下一步位置
		x = pos[0]
		y = pos[1]
		PLAYGROUND_WIDTH = 20
		PLAYGROUND_HEIGHT = 20  # 游戏区域大小
		if direction == "W":
			y -= 1
		if direction == "S":
			y += 1
		if direction == "A":
			x -= 1
		if direction == "D":
			x += 1
		if x < 0:
			x = PLAYGROUND_WIDTH - 1
		if x > PLAYGROUND_WIDTH - 1:
			x = 0
		if y < 0:
			y = PLAYGROUND_HEIGHT - 1
		if y > PLAYGROUND_HEIGHT - 1:
			y = 0
		return x, y
	
	def elude(self, pos, snakes):  # 躲避
		l = ["W", "S", "A", "D"]
		if self.next(l[0], pos) not in snakes:
			temp = l[0]
		elif self.next(l[1], pos) not in snakes:
			temp = l[1]
		elif self.next(l[2], pos) not in snakes:
			temp = l[2]
		elif self.next(l[3], pos) not in snakes:
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
		根据环境，通过决策算法返回前进的方向。这是决定策略类中必不可少的一个函数。
		:param game: 游戏
		:return: 决定的前进方向
		"""
		Hs = game.head_pos[0] - game.food_pos[0]  # 横向差值
		Vs = game.head_pos[1] - game.food_pos[1]  # 纵向差值
		
		if abs(Hs) > abs(Vs):
			if Hs < 0:
				temp = "D"
				if self.next(temp, game.head_pos) in game.snakes:
					return self.elude(game.head_pos, game.snakes)[0]
			else:
				temp = "A"
				if self.next(temp, game.head_pos) in game.snakes:
					return self.elude(game.head_pos, game.snakes)[0]
		else:
			if Vs < 0:
				temp = "S"
				if self.next(temp, game.head_pos) in game.snakes:
					return self.elude(game.head_pos, game.snakes)[0]
			else:
				temp = "W"
				if self.next(temp, game.head_pos) in game.snakes:
					return self.elude(game.head_pos, game.snakes)[0]
		return temp
