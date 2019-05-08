#!/usr/bin/env python3

__author__ = "Yxzh"

from random import randint


PLAYGROUND_WIDTH = 200
PLAYGROUND_HEIGHT = 200  # 游戏区域大小

class Snakey(object):
	
	def __init__(self, bomb = True):
		self.allow_bomb = bomb
		self.pos = [0, 0]  # 蛇头位置
		self.direction = "S"  # 上一步蛇头方向
		self.snakes = [(0, 0)] * 2  # 蛇数组
		self.isfood = True  # 食物判定
		self.bombs = []  # 炸弹数组
		self.food_pos = [randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10, randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10]  # 食物坐标
		self.ate = 0  # 食物计数
		self.deadflag = False  # 死亡判定
	
	def reset(self):
		self.pos = [0, 0]  # 蛇头位置
		self.direction = "S"  # 上一步蛇头方向
		self.snakes = [(0, 0)] * 2  # 蛇数组
		self.isfood = True  # 食物判定
		self.bombs = []  # 炸弹数组
		self.food_pos = [randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10,
		                 randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10]  # 食物坐标
		self.diffculty_counter = 0  # 难度计数
		self.ate = 0  # 食物计数
		self.deadflag = False  # 死亡判定
		
	def next(self, direction):
		"""
		蛇走一步
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
			self.pos[1] -= 10
		if self.direction == "S":
			self.pos[1] += 10
		if self.direction == "A":
			self.pos[0] -= 10
		if self.direction == "D":
			self.pos[0] += 10
		
		if self.pos[0] < 0:  # 碰到屏幕边缘循环
			self.pos[0] = PLAYGROUND_WIDTH - 10
		if self.pos[0] > PLAYGROUND_WIDTH - 10:
			self.pos[0] = 0
		if self.pos[1] < 0:
			self.pos[1] = PLAYGROUND_HEIGHT - 10
		if self.pos[1] > PLAYGROUND_HEIGHT - 10:
			self.pos[1] = 0
		
		del (self.snakes[0])  # 删除蛇数组顶
		
		if self.pos in self.snakes:  # 自身碰撞检测
			print("z")
			self.deadflag = True  # 触发死亡判定
		
		self.snakes.append((self.pos[0], self.pos[1]))  # 推入蛇数组底
		
		while (len(self.bombs) < 11) and self.allow_bomb:  # 刷新炸弹
			bomb_pos = [randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10, randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10]
			while (bomb_pos in self.snakes) or (self.food_pos[0] == bomb_pos[0] or self.food_pos[1] == bomb_pos[1]) or (
							  bomb_pos in self.bombs):  # 避免与蛇和食物和其他炸弹重叠刷新
				bomb_pos = [randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10, randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10]
			self.bombs.append(bomb_pos)
		
		if not self.isfood:  # 根据食物判定刷新食物
			self.food_pos = [randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10, randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10]
			while self.food_pos in self.snakes or self.food_pos in self.bombs:  # 避免重叠刷新
				self.food_pos = [randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10,
				                 randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10]
			self.isfood = True
		
		if self.pos in self.bombs and self.allow_bomb:  # 炸弹碰撞检测
			print("b")
			self.deadflag = True
		
		if self.pos == self.food_pos:  # 吃食物事件
			self.snakes.append([int(self.pos[0]), int(self.pos[1])])  # 将当前位置推入蛇数组
			self.ate += 1
			self.isfood = False
		
		return self.snakes, self.pos, self.food_pos, self.bombs, self.ate
