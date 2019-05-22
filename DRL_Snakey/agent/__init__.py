#!/usr/bin/env python3

__author__ = "Yxzh"

import DRL_Snakey.core


class Agent(object):
	def get_next_direction(self, Game: DRL_Snakey.core.Game):
		"""
		根据智能体对当前环境的判断选择下一步前进的方向。
		:return: 方向["W", "S", "A", "D"]
		"""
		pass
	
	def custom_function(self, Game: DRL_Snakey.core.Game):
		"""
		给不同的agnet预留的自定义函数，用来调试或数据可视化。
		"""
		pass
	
	# def visual_mode(self):
	def __str__(self):
		return "agent."
	
from .logic_AI import Logic
from .DP_AI import DP
from .MC_AI import MC