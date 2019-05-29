#!/usr/bin/env python3

__author__ = "TheVoid"

from DRL_Snakey.agent import Agent


class StupidAgent(Agent):

    def visual_mode(self, Game, pos):
        return 0

    def custom_function(self, Game):
        pass

    def get_next_direction(self, game):
        snake=game.main_snake
        x, y = snake.head_pos
        dir=snake.direction
        if dir == "S" and y==19:
            return "D"
        elif dir == "D" and y==19:
            return "W"
        elif dir == "W" and y==0:
            return "D"
        elif dir == "D" and y==0:
            return "S"
        else:
            return "S"

