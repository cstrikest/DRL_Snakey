#!/usr/bin/env python3

__author__ = "Yxzh"

class Snake(object):
	def __init__(self):
		self.head_pos = [0, 0]
		self.snakes = [(0, 0)] * 2
		self.direction = "S"
	