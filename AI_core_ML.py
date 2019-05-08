#!/usr/bin/env python3

__author__ = "Yxzh"

from tensorflow import keras
import numpy as np

class Snakey_AI(object):
	def __init__(self, model_path):
		self.model = keras.models.load_model(model_path)
		self.directions = ["W", "S", "A", "D"]
		
	def get_next_direction(self, input):
		return l[int(np.argmax(self.model.predict(input)))]