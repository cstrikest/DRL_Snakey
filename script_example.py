#!/usr/bin/env python3

__author__ = "Yxzh"

import DRL_Snakey as Snakey


game = Snakey.Game(0)
agent = Snakey.agent.DP(iteration = 10, walk_reward = -0.8)
UI = Snakey.UI(60)
UI.show(game, agent)
