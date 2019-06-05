#!/usr/bin/env python3

__author__ = "Yxzh"

import math
import DRL_Snakey
from DRL_Snakey.agent import Agent
from DRL_Snakey.core.snake import Snake
from DRL_Snakey.core import Game as Game_model
from DRL_Snakey.utils import *
from random import randint
from random import random


class MC(Agent):
	"""
	蒙特卡洛法，基于大量随机实验，决策前进方向。
	"""
	
	def __init__(self,
	             discount = 1,
	             iteration = 100,
	             max_step = 1000,
	             epsilon = 0.05,
	             walk_reward = -1,
	             eat_self_reward = -90,
	             food_reward = 60,):
		self.default_visual_mode = False
		self.discount = discount
		self.iteration = iteration
		self.max_step = max_step
		self.walk_reward = walk_reward
		self.eat_self_reward = eat_self_reward
		self.food_reward = food_reward
		self.strategy = DRL_Snakey.agent.Logic()
		self.epsilon = epsilon
	
	def get_next_direction(self, Game):
		direction_set = {}  # 各个方向的行动价值
		iteration_set = {}  # 各个方向进行尝试的次数
		passible_direction = list(DIRECTIONS)
		passible_direction.remove(get_opposite_direction(Game.main_snake.direction))  # 排除无效动作
		for each_first_direction in passible_direction:  # 建立字典
			direction_set[each_first_direction] = 0
			iteration_set[each_first_direction] = 1
		attempt_game = Game_model(0)
		for _ in range(0, self.iteration - 1):  # 开始随机尝试
			attempt_game.reset(bomb = 0,
			                   snake = Snake(list(Game.main_snake.head_pos),
			                                 list(Game.main_snake.snakes),
			                                 Game.main_snake.direction))
			attempt_game.food_pos = Game.food_pos
			first_direction = passible_direction[randint(0, 2)]
			if attempt_game.next_step(first_direction):
				direction_set[first_direction] += self.food_reward
			elif attempt_game.deathflag:
				direction_set[first_direction] += self.eat_self_reward
			else:
				direction_set[first_direction] += self.walk_reward
			power_of_discount = 1
			while True:
				direction = list(DIRECTIONS)
				direction.remove(get_opposite_direction(attempt_game.main_snake.direction))
				if random() <= self.epsilon:
					strategy = direction[randint(0, 2)]
				else:
					strategy = self.strategy.get_next_direction(attempt_game)
				power_of_discount += 1
				if attempt_game.next_step(strategy):
					direction_set[first_direction] += math.pow(self.discount, power_of_discount) * self.food_reward
					break
				elif attempt_game.deathflag:
					direction_set[first_direction] += math.pow(self.discount, power_of_discount) * self.eat_self_reward
					break
				# elif power_of_discount > self.max_step:
				# 	break
				else:
					direction_set[first_direction] += math.pow(self.discount, power_of_discount) * self.walk_reward
			iteration_set[first_direction] += 1
		for i in range(0, 3):
			direction_set[passible_direction[i]] = direction_set[passible_direction[i]] / iteration_set[
				passible_direction[i]]
		return max(direction_set, key = direction_set.get)
	
	def visual_mode(self, Game, pos):
		return 0
	
	def custom_function(self, Game):
		pass
