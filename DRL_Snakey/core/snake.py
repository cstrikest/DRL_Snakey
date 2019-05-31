#!/usr/bin/env python3

__author__ = "Yxzh"

from DRL_Snakey.utils import *

class Snake(object):
	def __init__(self, head_pos = None, snakes = None, direction = DIRECTIONS[1]):
		if head_pos is None:
			self.head_pos = [0, 0]
		else:
			self.head_pos = head_pos
		if snakes is None:
			self.snakes = [(0, 0)] * 2
		else:
			self.snakes = snakes
		self.direction = direction
		
	def __str__(self):
		return "Snake: " + str(self.snakes)
		