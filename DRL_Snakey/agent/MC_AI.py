#!/usr/bin/env python3

__author__ = "Yxzh"

import numpy as np
from DRL_Snakey.agent import Agent
from random import randint


class MC(Agent):
	def __init__(self, discount = 1, iteration = 20):
		self.discount = discount
		self.iteration = iteration
		
	def custom_function(self, Game):
		pass
	
	def get_next_direction(self, game):
		pass
	
