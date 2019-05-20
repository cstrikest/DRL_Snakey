#!/usr/bin/env python3

__author__ = "Yxzh"


class Agent(object):
	def get_next_direction(self, head_pos, food_pos, snakes, now_direction):
		"""
		根据智能体对当前环境的判断选择下一步前进的方向。
		:return: 方向["W", "S", "A", "D"]
		"""
		pass
	
	def custom_function(self, head_pos, food_pos, snakes, now_direction):
		"""
		给不同的agnet预留的自定义函数，用来调试或数据可视化。
		"""
		pass
	
	def __str__(self):
		return "Agent."
	
from .logic_AI import Logic
from .DP_AI import DP