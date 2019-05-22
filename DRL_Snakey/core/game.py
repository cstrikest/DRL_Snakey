#!/usr/bin/env python3

__author__ = "Yxzh"

from random import randint
import numpy as np


PLAYGROUND_WIDTH = 20
PLAYGROUND_HEIGHT = 20  # 游戏区域大小

class Game(object):
	def __init__(self, bomb = 0):
		"""
		初始化游戏
		:param bomb: 地图中炸弹数量
		"""
		self.bomb_number = bomb  # 炸弹个数
		self.head_pos = [0, 0]  # 蛇头位置
		self.direction = "S"  # 上一步蛇头方向
		self.snakes = [(0, 0)] * 2  # 蛇数组
		self.isfood = True  # 食物判定
		self.bombs = []  # 炸弹数组
		self.food_pos = (randint(0, PLAYGROUND_WIDTH - 1),
		                 randint(0, PLAYGROUND_HEIGHT - 1))  # 食物坐标
		self.ate = 0  # 食物计数
		self.deathflag = False  # 死亡判定
	
	def reset(self):
		"""
		重置游戏
		"""
		self.head_pos = [0, 0]  # 蛇头位置
		self.direction = "S"  # 上一步蛇头方向
		self.snakes = [(0, 0)] * 2  # 蛇数组
		self.isfood = True  # 食物判定
		self.bombs = []  # 炸弹数组
		self.food_pos = (randint(0, PLAYGROUND_WIDTH - 1),
		                 randint(0, PLAYGROUND_HEIGHT - 1))  # 食物坐标
		self.ate = 0  # 食物计数
		self.deathflag = False  # 死亡判定
	
	def next(self, direction):
		"""
		游戏进行一步
		:param direction: 每一步的方向
		:return: 返回详细信息
		"""
		
		if direction == "W" and self.direction != "S":
			self.direction = "W"
		if direction == "S" and self.direction != "W":
			self.direction = "S"
		if direction == "A" and self.direction != "D":
			self.direction = "A"
		if direction == "D" and self.direction != "A":
			self.direction = "D"
		if self.direction == "W":
			self.head_pos[1] -= 1
		if self.direction == "S":
			self.head_pos[1] += 1
		if self.direction == "A":
			self.head_pos[0] -= 1
		if self.direction == "D":
			self.head_pos[0] += 1
		if self.head_pos[0] < 0:  # 碰到屏幕边缘循环
			self.head_pos[0] = PLAYGROUND_WIDTH - 1
		if self.head_pos[0] > PLAYGROUND_WIDTH - 1:
			self.head_pos[0] = 0
		if self.head_pos[1] < 0:
			self.head_pos[1] = PLAYGROUND_HEIGHT - 1
		if self.head_pos[1] > PLAYGROUND_HEIGHT - 1:
			self.head_pos[1] = 0
		del (self.snakes[0])  # 删除蛇数组顶
		if (self.head_pos[0], self.head_pos[1]) in self.snakes:  # 自身碰撞检测
			self.deathflag = True  # 触发死亡判定
		self.snakes.append((self.head_pos[0], self.head_pos[1]))  # 推入蛇数组底
		while len(self.bombs) < self.bomb_number:  # 刷新炸弹
			bomb_pos = (randint(0, PLAYGROUND_WIDTH - 1), randint(0, PLAYGROUND_HEIGHT - 1))
			while (bomb_pos in self.snakes) or (self.food_pos[0] == bomb_pos[0] and self.food_pos[1] == bomb_pos[1]) or (
							  bomb_pos in self.bombs):  # 避免与蛇和食物和其他炸弹重叠刷新
				bomb_pos = (randint(0, PLAYGROUND_WIDTH - 1), randint(0, PLAYGROUND_HEIGHT - 1))
			self.bombs.append(bomb_pos)
		if (self.head_pos[0], self.head_pos[1]) == self.food_pos:  # 吃食物事件
			self.snakes.append((self.head_pos[0], self.head_pos[1]))  # 将当前位置推入蛇数组
			self.ate += 1
			self.isfood = False
		if not self.isfood:  # 根据食物判定刷新食物
			self.food_pos = (randint(0, PLAYGROUND_WIDTH - 1), randint(0, PLAYGROUND_HEIGHT - 1))
			while self.food_pos in self.snakes or self.food_pos in self.bombs:  # 避免重叠刷新
				self.food_pos = (randint(0, PLAYGROUND_WIDTH - 1),
				                 randint(0, PLAYGROUND_HEIGHT - 1))
			self.isfood = True
		if (self.head_pos[0], self.head_pos[1]) in self.bombs:  # 炸弹碰撞检测
			self.deathflag = True
		return self.snakes, self.head_pos, self.food_pos, self.bombs, self.ate
	
	def get_map(self, flat = False):
		"""
		获得游戏地图信息
		:return: 游戏地图信息，从左上到右下按行排列，将20×20的地图扁平化为400个地图数据。
				地图块上是蛇则标志为1，食物为2，炸弹为3，空为0，蛇与食物重叠则为-1。
		"""
		
		game_map = np.zeros((20, 20))
		for S in self.snakes:
			game_map[S] = 1
		for B in self.bombs:
			game_map[B] = 3
		if self.head_pos == self.food_pos:
			game_map[self.food_pos] = -1
		else:
			game_map[self.food_pos] = 2
		if flat:
			return game_map.reshape((400,))
		else:
			return game_map