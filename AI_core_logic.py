#!/usr/bin/env python3

import random

__author__ = "Yxzh"

PLAYGROUND_WIDTH = 20
PLAYGROUND_HEIGHT = 20  # 游戏区域大小
l = ["W", "S", "A", "D"]

def next(direction, pos):  # 预测下一步位置
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
		x = PLAYGROUND_WIDTH - 1
	if x > PLAYGROUND_WIDTH - 1:
		x = 0
	if y < 0:
		y = PLAYGROUND_HEIGHT - 1
	if y > PLAYGROUND_HEIGHT - 1:
		y = 0
	
	return (x, y)

def elude(pos, snakes):  # 躲避
	if next(l[0], pos) not in snakes:
		temp = l[0]
	elif next(l[1], pos) not in snakes:
		temp = l[1]
	elif next(l[2], pos) not in snakes:
		temp = l[2]
	elif next(l[3], pos) not in snakes:
		temp = l[3]
	else:
		temp = l[random.randrange(0, 4)]
	return temp

def get_next_direction(pos, food_pos, snakes):  # 追寻食物
	Hs = pos[0] - food_pos[0]  # 横向差值
	Vs = pos[1] - food_pos[1]  # 纵向差值
	
	if abs(Hs) > abs(Vs):
		if Hs < 0:
			temp = "D"
			if next(temp, pos) in snakes:
				return elude(pos, snakes)[0]
		else:
			temp = "A"
			if next(temp, pos) in snakes:
				return elude(pos, snakes)[0]
	else:
		if Vs < 0:
			temp = "S"
			if next(temp, pos) in snakes:
				return elude(pos, snakes)[0]
		else:
			temp = "W"
			if next(temp, pos) in snakes:
				return elude(pos, snakes)[0]
	return temp
