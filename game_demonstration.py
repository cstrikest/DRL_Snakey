#!/usr/bin/env python3

__author__ = "Yxzh"

import Snakey_core
import Snakey_UI_core
import AI_core_logic

UI = Snakey_UI_core.UI(False, 60)
Game = Snakey_core.Snakey(bomb = 0)
agent = AI_core_logic.Logic_AI()
UI.show(Game, agent)