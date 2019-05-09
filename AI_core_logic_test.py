#!/usr/bin/env python3

__author__ = "Yxzh"

import Snakey_core
import AI_core_logic
import time


print("Start.")
G = Snakey_core.Snakey(bomb = 0)  # 无炸弹模式
i = 0
max = 0
sum = 0
start = time.time()

agent = AI_core_logic.Logic_AI()
while i < 1000:
	while not G.deathflag:
		G.next(agent.get_next_direction(G.pos, G.food_pos, G.snakes))  # 获取下一步方向
	ate = G.ate
	print(ate)
	sum += ate
	if ate > max:
		max = ate
	G.reset()
	i += 1
			
print("\nmax ate: ", max)
print("average ate:", sum / i)
end = time.time()
print("use {} seconds, {} seconds per game".format(end - start, (end - start) / i))
