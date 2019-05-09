#!/usr/bin/env python3

__author__ = "Yxzh"

import Snakey_core
import AI_core_ML
import time


print("Start.")
G = Snakey_core.Snakey(bomb = 0)  # 无炸弹模式
ai = AI_core_ML.Snakey_AI("models/SnakeyAI.h5")
a = 10000
i = a
max = 0
sum = 0
start = time.time()

while True:
	G.next(ai.get_next_direction([G.pos, G.food_pos, G.snakes]))  # 获取下一步方向（假设）
	if G.deathflag:
		ate = G.ate
		print(ate)
		sum += ate
		if ate > max:
			max = ate
		G.reset()
		i -= 1
		if i is 0:
			break
print("\nmax ate: ", max)
print("average ate:", sum / a)
end = time.time()
print("use {} seconds, {} seconds per game".format(end - start, (end - start) / a))
