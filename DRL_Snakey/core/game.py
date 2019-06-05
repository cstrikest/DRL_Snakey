#!/usr/bin/env python3

__author__ = "Yxzh"

from random import randint
from DRL_Snakey.core.snake import Snake
from DRL_Snakey.utils import *
import numpy as np


PLAYGROUND_WIDTH = 20
PLAYGROUND_HEIGHT = 20  # 游戏区域大小

class Game(object):
	def __init__(self, bomb = 0, snake = Snake()):
		"""
		初始化游戏
		:param bomb: 地图中炸弹数量
		"""
		self.main_snake = snake
		self.bomb_number = bomb  # 炸弹个数
		self.isfood = True  # 食物判定
		self.bombs = []  # 炸弹数组
		self.food_pos = (randint(0, PLAYGROUND_WIDTH - 1),
		                 randint(0, PLAYGROUND_HEIGHT - 1))  # 食物坐标
		self.ate = 0  # 食物计数
		self.deathflag = False  # 死亡判定
		self.step = 0
	
	def reset(self, bomb = 0, snake = None):
		"""
		重置游戏
		"""
		if snake is None:
			self.main_snake = Snake()
		else:
			self.main_snake = snake
		self.bomb_number = bomb
		self.isfood = True  # 食物判定
		self.bombs = []  # 炸弹数组
		self.food_pos = (randint(0, PLAYGROUND_WIDTH - 1),
		                 randint(0, PLAYGROUND_HEIGHT - 1))  # 食物坐标
		self.ate = 0  # 食物计数
		self.deathflag = False  # 死亡判定
		self.step = 0
	
	def next_step(self, direction):
		"""
		游戏进行一步
	=	:param direction: 每一步的方向
		:return: 是否吃到食物
		"""
		
		is_ate = False
		if direction == DIRECTIONS[0] and self.main_snake.direction != DIRECTIONS[1]:
			self.main_snake.direction = DIRECTIONS[0]
		if direction == DIRECTIONS[1] and self.main_snake.direction != DIRECTIONS[0]:
			self.main_snake.direction = DIRECTIONS[1]
		if direction == DIRECTIONS[2] and self.main_snake.direction != DIRECTIONS[3]:
			self.main_snake.direction = DIRECTIONS[2]
		if direction == DIRECTIONS[3] and self.main_snake.direction != DIRECTIONS[2]:
			self.main_snake.direction = DIRECTIONS[3]
		if self.main_snake.direction == DIRECTIONS[0]:
			self.main_snake.head_pos[1] -= 1
		if self.main_snake.direction == DIRECTIONS[1]:
			self.main_snake.head_pos[1] += 1
		if self.main_snake.direction == DIRECTIONS[2]:
			self.main_snake.head_pos[0] -= 1
		if self.main_snake.direction == DIRECTIONS[3]:
			self.main_snake.head_pos[0] += 1
		if self.main_snake.head_pos[0] < 0:  # 碰到屏幕边缘循环
			self.main_snake.head_pos[0] = PLAYGROUND_WIDTH - 1
		if self.main_snake.head_pos[0] > PLAYGROUND_WIDTH - 1:
			self.main_snake.head_pos[0] = 0
		if self.main_snake.head_pos[1] < 0:
			self.main_snake.head_pos[1] = PLAYGROUND_HEIGHT - 1
		if self.main_snake.head_pos[1] > PLAYGROUND_HEIGHT - 1:
			self.main_snake.head_pos[1] = 0
		del (self.main_snake.snakes[0])  # 删除蛇数组顶
		if (self.main_snake.head_pos[0], self.main_snake.head_pos[1]) in self.main_snake.snakes:  # 自身碰撞检测
			self.deathflag = True  # 触发死亡判定
		self.main_snake.snakes.append((self.main_snake.head_pos[0], self.main_snake.head_pos[1]))  # 推入蛇数组底
		while len(self.bombs) < self.bomb_number:  # 刷新炸弹
			bomb_pos = (randint(0, PLAYGROUND_WIDTH - 1), randint(0, PLAYGROUND_HEIGHT - 1))
			while (bomb_pos in self.main_snake.snakes) or (self.food_pos[0] == bomb_pos[0] and self.food_pos[1] == bomb_pos[1]) or (
							  bomb_pos in self.bombs):  # 避免与蛇和食物和其他炸弹重叠刷新
				bomb_pos = (randint(0, PLAYGROUND_WIDTH - 1), randint(0, PLAYGROUND_HEIGHT - 1))
			self.bombs.append(bomb_pos)
		if (self.main_snake.head_pos[0], self.main_snake.head_pos[1]) == self.food_pos:  # 吃食物事件
			self.main_snake.snakes.append((self.main_snake.head_pos[0], self.main_snake.head_pos[1]))  # 将当前位置推入蛇数组
			self.ate += 1
			self.isfood = False
			is_ate = True
		if not self.isfood:  # 根据食物判定刷新食物
			self.food_pos = (randint(0, PLAYGROUND_WIDTH - 1), randint(0, PLAYGROUND_HEIGHT - 1))
			while self.food_pos in self.main_snake.snakes or self.food_pos in self.bombs:  # 避免重叠刷新
				self.food_pos = (randint(0, PLAYGROUND_WIDTH - 1),
				                 randint(0, PLAYGROUND_HEIGHT - 1))
			self.isfood = True
		if (self.main_snake.head_pos[0], self.main_snake.head_pos[1]) in self.bombs:  # 炸弹碰撞检测
			self.deathflag = True
		self.step += 1
		if self.step > 10000:
			self.step = 0
		return is_ate
	
	def get_map(self, flat = False):
		"""
		获得游戏地图信息
		:return: 游戏地图信息，从左上到右下按行排列，将20×20的地图扁平化为400个地图数据。
				地图块上是蛇则标志为1，食物为2，炸弹为3，空为0，蛇与食物重叠则为-1。
		"""
		
		game_map = np.zeros((20, 20))
		for S in self.main_snake.snakes:
			game_map[S] = 1
		for B in self.bombs:
			game_map[B] = 3
		if self.main_snake.head_pos == self.food_pos:
			game_map[self.food_pos] = -1
		else:
			game_map[self.food_pos] = 2
		if flat:
			return game_map.reshape((400,))
		else:
			return game_map