#!/usr/bin/env python3

__author__ = "Yxzh"

from .directions import *


def predict_next_position(direction, pos):
	"""
	根据方向返回下一步时点的坐标。
	:param direction: 方向
	:param pos: 当前坐标
	:return:
	"""
	x = pos[0]
	y = pos[1]
	if direction == DIRECTIONS[0]:
		y -= 1
	if direction == DIRECTIONS[1]:
		y += 1
	if direction == DIRECTIONS[2]:
		x -= 1
	if direction == DIRECTIONS[3]:
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