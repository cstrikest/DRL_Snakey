#!/usr/bin/env python3

__author__ = "Yxzh"


from DRL_Snakey.agent import Agent

class A_star(Agent):
	def __init__(self):
		self.open = []
		self.close = []
	