#!/usr/bin/env python3

__author__ = "Yxzh"

import DRL_Snakey as Snakey

game = Snakey.Game(0)
agent = Snakey.agent.MC()
UI = Snakey.UI(60)
UI.show(game, agent)