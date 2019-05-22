#!/usr/bin/env python3

__author__ = "Yxzh"


class Agent(object):
	default_visual_mode = False  # 使用此AI开始游戏时是否显示可视化界面，默认否。
	def get_next_direction(self, game):
		"""
		根据智能体对当前环境的判断选择下一步前进的方向。
		:return: 方向["W", "S", "A", "D"]
		"""
		pass
	
	def custom_function(self, Game):
		"""
		给不同的agnet预留的自定义函数，用来调试或数据可视化。
		"""
		pass
	
	def visual_mode(self, Game, pos):
		"""
		数据可视化预留函数。
		"""
		pass
	
from .logic_AI import Logic
from .DP_AI import DP
from .MC_AI import MC