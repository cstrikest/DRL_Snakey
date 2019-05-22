#!/usr/bin/env python3

__author__ = "Yxzh"

from DRL_Snakey.agent import Agent
import numpy as np


class DP(Agent):
	"""
	Dynamic Programming 动态规划-马尔科夫决策法
	通过迭代贝尔曼方程，每一步刷新地图各个点的价值，并且朝着价值最高的点前进。
	"""
	
	def __init__(self, discount = 1, iteration = 20, walk_reward = -1, eat_self_reward = -3, food_reward = 1):
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
		self.strategy = np.zeros((20, 20))
		self.iteration = iteration
		self.walk_reward = walk_reward
		self.eat_self_reward = eat_self_reward
		self.food_reward = food_reward
		self.strategy_max = 0
		self.strategy_min = 0
	
	def frash_state_value(self, Game):
		"""
		进行一次价值矩阵的计算迭代。
		:param Game: 游戏
		"""
		
		temp_action = ["W", "S", "A", "D"]
		temp_action.remove(self.get_opposite_direction(Game.direction))  # 排除无效动作，贪吃蛇游戏中是与前进方向相反的动作。
		for _ in range(0, self.iteration):
			temp_strategy = np.copy(self.strategy)
			for i in range(0, 20):
				for j in range(0, 20):
					temp = 0
					for a in temp_action:
						reward = self.walk_reward  # 每走一步默认回报
						x, y = self.next(a, (i, j))
						if (x, y) in Game.snakes[: -3]:
							reward = self.eat_self_reward  # 下一步吃到自己的回报
						if (x, y) == Game.food_pos:
							reward = self.food_reward  # 下一步吃到食物的回报
						temp += 1 / len(temp_action) * (reward + self.discount * self.strategy[x][y])
					temp_strategy[i][j] = temp
			temp_strategy[Game.food_pos[0]][Game.food_pos[1]] = 0  # 食物点价值最高
			self.strategy = temp_strategy
	
	def custom_function(self, Game):
		pass
	
	def next(self, direction, pos):
		"""
		根据方向返回下一步时点的坐标。
		:param direction: 方向
		:param pos: 当前坐标
		:return:
		"""
		x = pos[0]
		y = pos[1]
		if direction == "W":
			y -= 1
		if direction == "S":
			y += 1
		if direction == "A":
			x -= 1
		if direction == "D":
			x += 1
		if x < 0:
			x = 20 - 1
		if x > 20 - 1:
			x = 0
		if y < 0:
			y = 20 - 1
		if y > 20 - 1:
			y = 0
		return x, y
	
	@staticmethod
	def get_opposite_direction(now_direction):
		"""
		返回相对方向。用于排除无效的动作。（向上走时不能直接向下走）
		:param now_direction: 当前方向
		:return: 无效方向
		"""
		if now_direction == "W":
			return "S"
		if now_direction == "S":
			return "W"
		if now_direction == "A":
			return "D"
		if now_direction == "D":
			return "A"
	
	def visual_mode(self, Game, pos):
		"""
		返回指定点的标准化价值。
		:param Game: 游戏
		:param pos: 坐标
		:return: 标准化价值
		"""
		return (self.strategy[pos] - self.strategy_min) / (self.strategy_max - self.strategy_min)
	
	def get_next_direction(self, game):
		"""
		Agent类成员函数，根据当前环境进行决策并返回前进方向。
		:param game: 游戏
		:return: 决策方向
		"""
		self.strategy = np.zeros((20, 20))
		self.frash_state_value(game)
		temp_action = ["W", "S", "A", "D"]
		temp_action.remove(self.get_opposite_direction(game.direction))
		value = {}
		for a in temp_action:
			value[a] = self.strategy[self.next(a, game.head_pos)]
		optimal_solution = max(value, key = value.get)
		self.strategy_max = self.strategy.max()
		self.strategy_min = self.strategy.min()
		return optimal_solution
