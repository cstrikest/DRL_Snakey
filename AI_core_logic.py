#!/usr/bin/env python3

__author__ = "Yxzh"

def get_next_direction(pos, food_pos):
		Hs = pos[0] - food_pos[0]  # 横向差值
		Vs = pos[1] - food_pos[1]  # 纵向差值
		if abs(Hs) > abs(Vs):
			if Hs < 0:
				return "D"
			else:
				return "A"
		else:
			if Vs < 0:
				return "S"
			else:
				return "W"
