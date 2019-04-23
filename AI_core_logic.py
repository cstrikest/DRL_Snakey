#!/usr/bin/env python3

__author__ = "Yxzh"

import random


def next(direction, pos):
	if direction == "W":
		pos[1] -= 10
	if direction == "S":
		pos[1] += 10
	if direction == "A":
		pos[0] -= 10
	if direction == "D":
		pos[0] += 10
	
	return tuple(pos)

def get_next_direction(pos, food_pos, snakes):
	l = ["W", "S", "A", "D"]
	Hs = pos[0] - food_pos[0]  # 横向差值
	Vs = pos[1] - food_pos[1]  # 纵向差值
	
	if abs(Hs) > abs(Vs):
		if Hs < 0:
			temp = "D"
			if next(temp, pos) in snakes:
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
					print("????")
		else:
			temp = "A"
			if next(temp, pos) in snakes:
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
					print("????")
	else:
		if Vs < 0:
			temp = "S"
			if next(temp, pos) in snakes:
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
					print("????")
		else:
			temp = "W"
			if next(temp, pos) in snakes:
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
					print("????")
	return temp
