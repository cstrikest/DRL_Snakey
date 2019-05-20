#!/usr/bin/env python3

__author__ = "Yxzh"

from DRL_Snakey.Agent import Agent
import numpy as np
import matplotlib.pyplot as plt


class DP(Agent):
	"""
	Dynamic Programming 动态规划-马尔科夫决策法
	通过迭代贝尔曼方程，每一步刷新地图各个点的价值，并且朝着价值最高的点前进。
	"""
	def __init__(self, discount, iteration, walk_reward, eat_self_reward, food_reward):
		"""
		构造DP智能体类。
		:param discount: 衰减率，贝尔曼方程中对于非即时回报的衰减率。
		:param iteration: 推算价值矩阵的迭代次数。
		:param walk_reward: 每走一步的回报
		:param eat_self_reward: 吃到自己的回报
		:param food_reward: 吃到食物的回报
		"""
		self.discount = discount
		self.strategy = np.zeros((20, 20))
		self.range = (20, 20)
		self.iteration = iteration
		self.walk_reward = walk_reward
		self.eat_self_reward = eat_self_reward
		self.food_reward = food_reward
	
	def frash_state_value(self, food_pos, snakes, now_direction, head_pos):
		"""
		进行一次价值矩阵的计算迭代。
		:param food_pos: 食物坐标
		:param snakes: 蛇数组
		:param now_direction: 当前方向，用于排除无效的动作。
		:param head_pos: 蛇头坐标
		:return: 当前的价值矩阵
		"""
		temp_strategy = np.copy(self.strategy)
		temp_action = ["W", "S", "A", "D"]
		temp_action.remove(self.get_opposite_direction(now_direction))  # 排除无效动作，贪吃蛇游戏中是与前进方向相反的动作。
		for i in range(0, self.range[0]):
			for j in range(0, self.range[1]):
				temp = 0
				for a in temp_action:
					reward = self.walk_reward  # 每走一步默认回报
					if self.next(a, (i, j)) in snakes[: -1]:
						reward = self.eat_self_reward  # 下一步吃到自己的回报
					if self.next(a, (i, j)) == food_pos:
						reward = self.food_reward  # 下一步吃到食物的回报
					temp += 1 / len(temp_action) * (reward + self.discount * self.get_strategy(self.strategy, a, [i, j]))
				temp_strategy[i][j] = temp
		temp_strategy[food_pos[0]][food_pos[1]] = 0  # 食物点价值最高
		self.strategy = temp_strategy
		return self.strategy
	
	def get_strategy(self, strategy, action, strategy_pos):
		"""
		根据方向获取下一个点的价值。
		:param strategy: 价值矩阵
		:param action: 动作方向
		:param strategy_pos: 作用位置
		:return: 下一个点的价值
		"""
		if action == "A":
			if strategy_pos[0] == 0:
				return strategy[self.range[0] - 1][strategy_pos[1]]
			else:
				return strategy[strategy_pos[0] - 1][strategy_pos[1]]
		if action == "D":
			if strategy_pos[0] == self.range[0] - 1:
				return strategy[0][strategy_pos[1]]
			else:
				return strategy[strategy_pos[0] + 1][strategy_pos[1]]
		if action == "W":
			if strategy_pos[1] == 0:
				return strategy[strategy_pos[0]][self.range[1] - 1]
			else:
				return strategy[strategy_pos[0]][strategy_pos[1] - 1]
		if action == "S":
			if strategy_pos[1] == self.range[1] - 1:
				return strategy[strategy_pos[0]][0]
			else:
				return strategy[strategy_pos[0]][strategy_pos[1] + 1]
		if action == "N":
			return strategy[strategy_pos[0]][strategy_pos[1]]
	
	def next(self, direction, pos):
		"""
		根据方向返回下一个点的坐标。
		:param direction: 方向
		:param pos: 当前点
		:return: 下一个点
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
			x = self.range[0] - 1
		if x > self.range[0] - 1:
			x = 0
		if y < 0:
			y = self.range[1] - 1
		if y > self.range[1] - 1:
			y = 0
		return x, y
	
	def custom_function(self, head_pos, food_pos, snakes, now_direction):
		"""
		Agent类成员函数，保有的自定义函数。这里为输出价值矩阵的可视化图。此函数会重新计算价值矩阵。
		:param head_pos: 蛇头坐标
		:param food_pos: 食物坐标
		:param snakes: 蛇数组
		:param now_direction: 当前方向
		"""
		self.strategy = np.zeros((20, 20))
		for _ in range(0, self.iteration):
			self.frash_state_value(food_pos, snakes, now_direction, head_pos)
		plt.matshow(self.strategy.T)
		plt.colorbar()
		plt.title(str(food_pos))
		plt.show()
	
	def get_opposite_direction(self, now_direction):
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
	
	def get_next_direction(self, head_pos, food_pos, snakes, now_direction):
		"""
		Agent类成员函数，根据当前环境进行决策并返回前进方向。
		:param head_pos: 蛇头坐标
		:param food_pos: 食物坐标
		:param snakes: 蛇数组
		:param now_direction: 当前方向
		:return: 决策方向
		"""
		self.strategy = np.zeros((20, 20))
		for _ in range(0, self.iteration):
			self.frash_state_value(food_pos, snakes, now_direction, head_pos)
		temp_action = ["W", "S", "A", "D"]
		temp_action.remove(self.get_opposite_direction(now_direction))
		value = {}
		for a in temp_action:
			value[a] = self.get_strategy(self.strategy, a, head_pos)
		optimal_solution = max(value, key = value.get)
		return optimal_solution
