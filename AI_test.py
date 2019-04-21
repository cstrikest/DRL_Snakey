#!/usr/bin/env python3

__author__ = "Yxzh"

from Snacky_core import Snakey
from time import sleep


S = Snakey()

while True:
	Hs = S.pos[0] - S.food_pos[0]  # 横向差值
	Vs = S.pos[1] - S.food_pos[1]  # 纵向差值
	
	if abs(Hs) > abs(Vs):
		if Hs < 0:
			print("D")
			print(S.next("D"))
		else:
			print("A")
			print(S.next("A"))
	else:
		if Vs < 0:
			print("S")
			print(S.next("S"))
		else:
			print("W")
			print(S.next("W"))
	
	if S.deadflag:
		print("Dead.")
		break
