#!/usr/bin/env python3

__author__ = "Yxzh"

from DRL_Snakey.utils import *
from DRL_Snakey.agent import Agent
import numpy as np


class DP(Agent):
	"""
	Dynamic Programming 动态规划-马尔科夫决策法
	通过迭代贝尔曼方程，每一步刷新地图各个点的价值，并且朝着价值最高的点前进。
	"""
	def __init__(self, discount = 1, iteration = 10, walk_reward = -0.8, eat_self_reward = -4, food_reward = 1):
		"""
		构造DP智能体类。
		:param discount: 衰减率，贝尔曼方程中对于非即时回报的衰减率。
		:param iteration: 推算价值矩阵的迭代次数。
		:param walk_reward: 每走一步的回报
		:param eat_self_reward: 吃到自己的回报
		:param food_reward: 吃到食物的回报
		"""
		self.default_visual_mode = True
		self.discount = discount
		self.values= np.zeros((20, 20))
		self.iteration = iteration
		self.walk_reward = walk_reward
		self.eat_self_reward = eat_self_reward
		self.food_reward = food_reward
		self.value_max = 0
		self.value_min = 0
	
	def frash_state_value(self, Game):
		"""
		进行一次价值矩阵的计算迭代。
		:param Game: 游戏
		"""
		temp_action = list(DIRECTIONS)
		temp_action.remove(get_opposite_direction(Game.main_snake.direction))  # 排除无效动作，贪吃蛇游戏中是与前进方向相反的动作。
		for _ in range(0, self.iteration):
			temp_value = np.copy(self.values)
			for i in range(0, 20):
				for j in range(0, 20):
					temp = 0
					for a in temp_action:
						reward = self.walk_reward  # 每走一步默认回报
						x, y = predict_next_position(a, (i, j))
						if (x, y) in Game.main_snake.snakes[: -3]:
							reward = self.eat_self_reward  # 下一步吃到自己的回报
						if (x, y) == Game.food_pos:
							reward = self.food_reward  # 下一步吃到食物的回报
						temp += 1 / len(temp_action) * (reward + self.discount * self.values[x][y])
					temp_value[i][j] = temp
			temp_value[Game.food_pos[0]][Game.food_pos[1]] = 0  # 食物点价值最高
			self.values = temp_value
			
	
	def button_K_e_pressed(self, Game):
		print("Please press 'F' in game switch to visualize mode.")
	
	def visual_mode(self, Game, pos):
		"""
		返回指定点的标准化价值。
		:param Game: 游戏
		:param pos: 坐标
		:return: 标准化价值
		"""
		return (self.values[pos] - self.value_min) / (self.value_max - self.value_min)
	
	def get_next_direction(self, game):
		"""
		Agent类成员函数，根据当前环境进行决策并返回前进方向。
		:param game: 游戏
		:return: 决策方向
		"""
		self.values = np.zeros((20, 20))
		self.frash_state_value(game)
		temp_action = list(DIRECTIONS)
		temp_action.remove(get_opposite_direction(game.main_snake.direction))
		strategy = {}
		for a in temp_action:
			strategy[a] = self.values[predict_next_position(a, game.main_snake.head_pos)]
		optimal_solution = max(strategy, key = strategy.get)
		self.value_max = self.values.max()
		self.value_min = self.values.min()
		return optimal_solution
