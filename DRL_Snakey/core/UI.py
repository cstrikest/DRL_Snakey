#!/usr/bin/env python3

__author__ = "Yxzh"

import pygame
import sys
from pygame.locals import *
from pygame.color import THECOLORS
import pygame.font

path = __file__.replace("core/UI.py", "")

class UI(object):
	def __init__(self, visual_mode = True, fps = 60):
		"""
		初始化游戏界面。
		:param visual_mode: 可视化模式
		:param fps: 游戏帧率
					根据计算性能，会有实际帧率低于设定帧率的情况。
		"""
		self.PLAYGROUND_WIDTH = 20
		self.PLAYGROUND_HEIGHT = 20  # 游戏区域大小
		self.INFOAREA_WIDTH = 100
		self.INFOAREA_HEIGHT = 200  # 信息区域大小
		self.s_screen = pygame.display.set_mode(
			(self.PLAYGROUND_WIDTH * 10 + self.INFOAREA_WIDTH, self.PLAYGROUND_HEIGHT * 10), 0,
			32)
		self.visual_mode = visual_mode  # 显示模式 0为默认 1为图像模式
		WINDOW_TITLE = "Snacky"  # 屏幕标题
		allowed_event = [pygame.KEYDOWN, pygame.QUIT]  # 事件列表
		pygame.init()  # 初始化pygame
		pygame.display.set_caption(WINDOW_TITLE)  # 窗口标题
		self.fps_clock = pygame.time.Clock()  # 创建FPS时钟对象
		pygame.event.set_allowed(allowed_event)  # 设置事件过滤
		self.is_pause = False
		self.s_infoarea = pygame.Surface((self.PLAYGROUND_WIDTH * 5, self.PLAYGROUND_HEIGHT * 10), 0, 32)  # 信息区域Surface
		self.s_pltarea = pygame.Surface((self.PLAYGROUND_WIDTH * 10, self.PLAYGROUND_HEIGHT * 10), 0, 32)  # 图表区域Surface
		self.si_snake = pygame.image.load(path + "images/snake.png").convert_alpha()  # 加载图片
		self.si_food = pygame.image.load(path + "images/Pineapple.png").convert_alpha()
		self.si_deadsnake = pygame.image.load(path + "images/dead_snake.png").convert_alpha()
		self.si_gamestart = pygame.image.load(path + "images/game_start.png").convert_alpha()
		self.si_bomb = pygame.image.load(path + "images/bm.png").convert_alpha()
		pygame.font.init()  # 初始化字体
		f_arial = pygame.font.SysFont("arial", 24)  # 加载字体
		f_optima = pygame.font.SysFont("optima", 35)
		f_small_arial = pygame.font.SysFont("arial", 12, 1)
		self.sf_arial_gameover = f_arial.render("GAMEOVER!", 1, THECOLORS["black"])  # 渲染文字
		self.sf_arial_scoreboad = f_arial.render("SCOREBOARD", 1, THECOLORS["black"])
		self.sf_small_arial_restart = f_small_arial.render("Press 'R' to restart.", 1, THECOLORS["black"])
		self.sf_small_arial_scoreboard = f_small_arial.render("Press 'S' to open Scoreboard.", 1, THECOLORS["black"])
		self.sf_small_arial_gamestart = f_small_arial.render("SPACE to start and 'Q' to exit.", 1, THECOLORS["black"])
		self.sf_small_arial_back = f_small_arial.render("Press 'R' to return.", 1, THECOLORS["black"])
		self.sf_small_arial_score = f_small_arial.render("Score: ", 1, THECOLORS["red"])
		self.sf_optima_caption = f_optima.render("SNACKY", 1, THECOLORS["orange"])
		self.sf_small_arial_level = f_small_arial.render("level: ", 1, THECOLORS["black"])
		self.sf_small_arial_current_fps = f_small_arial.render("fps: ", 1, THECOLORS["black"])
		self.sf_small_arial_ate = f_small_arial.render("ate: ", 1, THECOLORS["black"])
		self.sf_small_arial_position = f_small_arial.render("pos: ", 1, THECOLORS["black"])
		self.sf_small_arial_botton = f_small_arial.render("btnreg: ", 1, THECOLORS["black"])
		self.sf_small_arial_direction = f_small_arial.render("direction: ", 1, THECOLORS["black"])
		self.sf_small_arial_dot = f_small_arial.render(".", 1, THECOLORS["black"])
		self.Lsf_small_arial_direction = {
			"W": f_small_arial.render("W", 1, THECOLORS["black"]),
			"S": f_small_arial.render("S", 1, THECOLORS["black"]),
			"A": f_small_arial.render("A", 1, THECOLORS["black"]),
			"D": f_small_arial.render("D", 1, THECOLORS["black"]),
		}
		self.Lsf_small_arial_numbers_black = []
		for i in range(0, 10):
			self.Lsf_small_arial_numbers_black.append(f_small_arial.render(str(i), 1, THECOLORS["black"]))
		self.fps = fps  # 帧率
	
	def show(self, game, agent):
		"""
		显示图形界面。
		:param game: 游戏物理引擎类
		:param agent: 决策逻辑类
		"""
		if agent.default_visual_mode:
			self.s_screen = pygame.display.set_mode(
				(self.PLAYGROUND_WIDTH * 20 + self.INFOAREA_WIDTH, self.PLAYGROUND_HEIGHT * 10), 0,
				32)
		else:
			self.s_screen = pygame.display.set_mode(
				(self.PLAYGROUND_WIDTH * 10 + self.INFOAREA_WIDTH, self.PLAYGROUND_HEIGHT * 10), 0,
				32)
		self.start()  # 开始游戏画面
		while True:  # 屏幕循环
			for event in pygame.event.get():  # 事件循环
				if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_q:  # 退出事件
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN and event.key == K_e:
					agent.custom_function(game)
				if event.type == KEYDOWN and event.key == K_f:
					if self.visual_mode:
						self.s_screen = pygame.display.set_mode(
							(self.PLAYGROUND_WIDTH * 10 + self.INFOAREA_WIDTH, self.PLAYGROUND_HEIGHT * 10), 0,
							32)
						self.visual_mode = False
					else:
						self.s_screen = pygame.display.set_mode(
							(self.PLAYGROUND_WIDTH * 20 + self.INFOAREA_WIDTH, self.PLAYGROUND_HEIGHT * 10), 0,
							32)
						self.visual_mode = True
				
				if event.type == KEYDOWN and event.key == K_p:
					self.pause()
			self.s_screen.fill(THECOLORS["white"])  # 填充白屏
			game.next(agent.get_next_direction(game))  # 获取下一步方向
			if self.visual_mode:  # 可视化模式
				for i in range(0, 20):
					for j in range(0, 20):
						pygame.draw.rect(self.s_screen, [agent.visual_mode(game, (i, j)) * 255] * 3,
						                 [i * 10 + 300, j * 10, 10, 10], 0)
			pygame.draw.line(self.s_screen, THECOLORS["black"], (300, 0), (300, 200), 2)
			self.s_screen.blit(self.si_food, (game.food_pos[0] * 10 - 4, game.food_pos[1] * 10 - 5))  # 填充食物图片
			for i in game.bombs:  # 填充炸弹图片
				self.s_screen.blit(self.si_bomb, [x * 10 - 2 for x in i])
			for i in game.snakes:  # 填充蛇图片
				self.s_screen.blit(self.si_snake, [x * 10 for x in i])
			if game.deathflag:  # 死亡判定
				self.f_gameover(game.ate)  # 游戏结束画面
				game.reset()
			self.s_infoarea.fill(THECOLORS["gray"])  # 开始填充信息区域各种信息
			pygame.draw.line(self.s_infoarea, THECOLORS["black"], (0, 0), (0, self.INFOAREA_HEIGHT), 3)  # 分隔线
			self.s_infoarea.blit(self.sf_small_arial_level, (10, 5))  # 难度信息提示
			self.s_infoarea.blit(self.sf_small_arial_ate, (10, 20))  # 食物数量信息
			self.s_infoarea.blit(self.sf_small_arial_position, (10, 35))  # 位置信息
			self.s_infoarea.blit(self.sf_small_arial_direction, (10, 65))  # 方向信息
			self.s_infoarea.blit(self.sf_small_arial_botton, (10, 80))  # 按键寄存信息 （实时刷新）
			self.s_infoarea.blit(self.sf_small_arial_current_fps, (10, 95))  # FPS（实时刷新）
			self.s_infoarea.blit(self.sf_small_arial_dot, (65, 5))
			self.f_show_number(self.s_infoarea, game.ate, (65, 20))
			self.f_show_number(self.s_infoarea, game.head_pos[0], (65, 35))
			self.f_show_number(self.s_infoarea, game.head_pos[1], (65, 50))
			current_fps = self.fps_clock.get_fps()  # 获取实时FPS
			self.f_show_number(self.s_infoarea, current_fps, (65, 95))  # 填充FPS
			self.s_infoarea.blit(self.Lsf_small_arial_direction[game.direction], (65, 65))
			self.s_infoarea.blit(self.Lsf_small_arial_direction[game.direction], (65, 80))  # 填充按键寄存
			self.s_screen.blit(self.s_infoarea, (self.PLAYGROUND_WIDTH * 10, 0))  # 将实时填充后的信息Surface填充至屏幕Surface
			pygame.display.flip()  # 将图像内存缓冲刷新至屏幕
			self.fps_clock.tick(self.fps)  # FPS等待时钟
			if self.is_pause:
				self.pause()
	
	def f_show_number(self, surface, number, position):
		"""
		在目标Surface上填充数字
		:param surface: 目标Surface
		:param number: 数字
		:param position: 位置
		"""
		
		surface.blit(self.Lsf_small_arial_numbers_black[int(number / 100)], (position[0], position[1]))
		surface.blit(self.Lsf_small_arial_numbers_black[int((number % 100) / 10)], (position[0] + 7, position[1]))
		surface.blit(self.Lsf_small_arial_numbers_black[int((number % 100) % 10)], (position[0] + 14, position[1]))
		return
	
	def start(self):
		"""
		游戏开始画面
		"""
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_q):  # 退出事件
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN and event.key == K_s:  # 进入计分板画面
					self.f_scoreboard()
				if event.type == pygame.KEYDOWN and event.key == K_SPACE:  # 进入main()函数
					return
			self.s_screen.fill(THECOLORS["white"])
			self.s_screen.blit(self.sf_optima_caption, (81, 3))
			self.s_screen.blit(self.si_gamestart, (93, 90))
			self.s_screen.blit(self.sf_small_arial_gamestart, (62, 52))
			self.s_screen.blit(self.sf_small_arial_scoreboard, (62, 70))
			pygame.display.flip()
			self.fps_clock.tick(5)
	
	def f_gameover(self, ate):
		"""
		游戏结束画面
		:param ate: 食物计数
		"""
		
		fi_score = open("score.s", "a+")  # 将分数写入分数文件 不存在就新建
		fi_score.write(str(ate) + "\n")
		fi_score.close()  # 关闭文件IO流
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_q:  # 退出事件
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN and event.key == K_s:  # 进入计分板画面
					self.f_scoreboard()
				if event.type == pygame.KEYDOWN and event.key == K_r:  # 重新开始
					return
			self.s_screen.fill(THECOLORS["white"])
			self.s_screen.blit(self.sf_arial_gameover, (72, 4))
			self.s_screen.blit(self.sf_small_arial_score, (100, 35))
			self.s_screen.blit(self.sf_small_arial_restart, (92, 50))
			self.s_screen.blit(self.sf_small_arial_scoreboard, (62, 65))
			self.s_screen.blit(self.si_deadsnake, (80, 75))
			self.f_show_number(self.s_screen, ate, (150, 35))  # 填充该局得分
			pygame.display.flip()
			self.fps_clock.tick(5)
	
	def f_scoreboard(self):  # 计分板画面
		"""
		计分板画面
		"""
		
		fi_score = open("score.s", "r")  # 读取分数文件
		scores = []
		for i in fi_score.readlines():  # 转换为int
			scores.append(int(i))
		fi_score.close()
		scores.sort(reverse = True)  # 倒序排列
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_q:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN and event.key == K_r:  # 重新开始
					return
			self.s_screen.fill(THECOLORS["white"])
			self.s_screen.blit(self.sf_arial_scoreboad, (65, 4))
			self.s_screen.blit(self.sf_small_arial_back, (100, 40))
			for i in range(0, len(scores)):  # 填充排行榜
				self.s_screen.blit(self.Lsf_small_arial_numbers_black[i + 1], (130, 60 + 15 * i))
				self.s_screen.blit(self.sf_small_arial_dot, (137, 60 + 15 * i))
				self.f_show_number(self.s_screen, scores[i], (150, 60 + 15 * i))
				if i > 7:
					break
			pygame.display.flip()
			self.fps_clock.tick(5)
	
	def pause(self):  # 暂停
		"""
		暂停游戏，方便查看当前状态。
		"""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_q:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN and event.key == K_p:  # 继续
					self.is_pause = False
					return
				if event.type == pygame.KEYDOWN and event.key == K_n:
					self.is_pause = True
					return
