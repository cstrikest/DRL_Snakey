#!/usr/bin/env python3

__author__ = "Yxzh"

from Snacky_core import Snakey
from time import sleep
from random import randrange

S = Snakey()
d = ["W", "S", "A", "D"]
def fd():
	while True:
		for i in range(0, 4):
			yield d[i]
			
S.start()
while True:
	print(S.next("D"))
	sleep(0.2)
	if S.deadflag:
		break