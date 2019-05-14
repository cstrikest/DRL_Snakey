#!/usr/bin/env python3

__author__ = "Yxzh"


class Agent(object):
	def get_next_direction(self, pos, food_pos, snakes):
		"""
		根据智能体对当前环境的判断选择下一步前进的方向。
		:return: 方向["W", "S", "A", "D"]
		"""
		pass
	
	def __str__(self):
		return "Agent."
	
from .logic_AI import Logic
from .DRL_AI import DRL