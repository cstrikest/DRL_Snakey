import pygame
import sys
from pygame.locals import *
from pygame.color import THECOLORS
import pygame.font
from random import randint


INFOAREA_WIDTH = 100
INFOAREA_HEIGHT = 200  # 屏幕大小
PLAYGROUND_WIDTH = 200
PLAYGROUND_HEIGHT = 200
WINDOW_TITLE = "Snacky"  # 屏幕标题
allowed_event = [pygame.KEYDOWN, pygame.QUIT]  # 有用事件列表
pygame.init()  # 初始化pygame
pygame.display.set_caption(WINDOW_TITLE)  # 窗口标题
fps_clock = pygame.time.Clock()  # 创建FPS计数器
pygame.event.set_allowed(allowed_event)
s_screen = pygame.display.set_mode((PLAYGROUND_WIDTH + INFOAREA_WIDTH, PLAYGROUND_HEIGHT), 0, 32)  # 创建屏幕Surface
# s_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN, 0, 32)
s_infoarea = pygame.Surface((PLAYGROUND_WIDTH, PLAYGROUND_HEIGHT), 0, 32)

si_snake = pygame.image.load("images/snake.png").convert_alpha()  # 加载图片
si_food = pygame.image.load("images/Pineapple.png").convert_alpha()
si_deadsnake = pygame.image.load("images/dead_snake.png").convert_alpha()
si_gamestart = pygame.image.load("images/game_start.png").convert_alpha()
si_bomb = pygame.image.load("images/bm.png").convert_alpha()

pygame.font.init()  # 初始化字体
f_arial = pygame.font.SysFont("arial", 24)  # 加载字体
f_optima = pygame.font.SysFont("optima", 35)
f_small_arial = pygame.font.SysFont("arial", 12, 1)

sf_arial_gameover = f_arial.render("GAMEOVER!", 1, THECOLORS["black"])  # 渲染文字
sf_small_arial_restart = f_small_arial.render("Press 'R' to restart.", 1, THECOLORS["black"])
sf_small_arial_scoreboard = f_small_arial.render("Press 'S' to open Scoreboard.", 1, THECOLORS["black"])
sf_small_arial_gamestart = f_small_arial.render("SPACE to start and 'Q' to exit.", 1, THECOLORS["black"])
sf_optima_caption = f_optima.render("SNACKY", 1, THECOLORS["orange"])
sf_small_arial_level = f_small_arial.render("level: ", 1, THECOLORS["black"])
sf_small_arial_length = f_small_arial.render("length: ", 1, THECOLORS["black"])
sf_small_arial_ate = f_small_arial.render("ate: ", 1, THECOLORS["black"])
sf_small_arial_position = f_small_arial.render("pos: ", 1, THECOLORS["black"])
sf_small_arial_botton = f_small_arial.render("btnreg: ", 1, THECOLORS["black"])
sf_small_arial_direction = f_small_arial.render("direction: ", 1, THECOLORS["black"])
Lsf_small_arial_numbers_black = []
Lsf_small_arial_numbers_red = []
for i in range(0, 10):
	Lsf_small_arial_numbers_black.append(f_small_arial.render(str(i), 1, THECOLORS["black"]))
for i in range(0, 10):
	Lsf_small_arial_numbers_red.append(f_small_arial.render(str(i), 1, THECOLORS["red"]))

def main():
	fps = 60  # 帧率
	pos_x = 0  # 蛇头位置
	pos_y = 0
	button = "N"  # 按键寄存
	direction = "S"  # 蛇头方向
	snakes = [(0, 0)] * 2 # 蛇数组
	isfood = False  # 场上是否存在食物
	bombs = []  # 炸弹数组
	food_pos_x = 0  # 食物坐标
	food_pos_y = 0
	diffculty_counter = 0  # 难度计数
	ate = 0
	level = 5  # 难度
	c_frame = 0  # 空闲帧数计数器
	diffculty = [14, 12, 10, 8, 6, 5, 4, 3, 2, 1, 0]  # 难度表 越难空闲帧越少
	deadflag = False

	f_gamestart(s_screen, fps_clock, fps)  # 开始游戏

	while True:  # 屏幕循环
		for event in pygame.event.get():  # 处理事件
			if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_q:  # 退出事件
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN and event.key == K_s:  # 按键事件 调整蛇头方向
				button = "S"
			if event.type == KEYDOWN and event.key == K_d:
				button = "D"
			if event.type == KEYDOWN and event.key == K_w:
				button = "W"
			if event.type == KEYDOWN and event.key == K_a:
				button = "A"

		if c_frame > diffculty[level]:
			if button == "W" and direction != "S":
				direction = "W"
			if button == "S" and direction != "W":
				direction = "S"
			if button == "A" and direction != "D":
				direction = "A"
			if button == "D" and direction != "A":
				direction = "D"

			if direction == "W":  # 自动前进
				pos_y -= 10
			if direction == "S":
				pos_y += 10
			if direction == "A":
				pos_x -= 10
			if direction == "D":
				pos_x += 10

			if pos_x < 0:  # 碰到屏幕边缘循环
				pos_x = PLAYGROUND_WIDTH - 10
			if pos_x > PLAYGROUND_WIDTH - 10:
				pos_x = 0
			if pos_y < 0:
				pos_y = PLAYGROUND_HEIGHT - 10
			if pos_y > PLAYGROUND_HEIGHT - 10:
				pos_y = 0

			del (snakes[0])  # 蛇数组处理

			if (pos_x, pos_y) in snakes:  # 碰撞检测
				deadflag = True  # 游戏结束

			snakes.append((pos_x, pos_y))

			if len(bombs) < level:
				bomb_pos_x = randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10
				bomb_pos_y = randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10

				while ((bomb_pos_x, bomb_pos_y) in snakes) or (
								  food_pos_x == bomb_pos_x or food_pos_y == bomb_pos_y) or (
								  (bomb_pos_x, bomb_pos_y) in bombs):
					bomb_pos_x = randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10
					bomb_pos_y = randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10

				bombs.append((bomb_pos_x, bomb_pos_y))

			if not isfood:
				food_pos_x = randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10
				food_pos_y = randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10

				while (food_pos_x, food_pos_y) in snakes or (food_pos_x, food_pos_y) in bombs:
					food_pos_x = randint(0, PLAYGROUND_WIDTH / 10 - 1) * 10
					food_pos_y = randint(0, PLAYGROUND_HEIGHT / 10 - 1) * 10

				isfood = True

			if (pos_x, pos_y) in bombs:
				deadflag = True

			if pos_x == food_pos_x and pos_y == food_pos_y:  # 吃食物事件
				snakes.append((pos_x, pos_y))
				diffculty_counter += 1
				ate += 1
				isfood = False

			if diffculty_counter > 4:  # 难度调整
				if level < len(diffculty):
					level += 1
					diffculty_counter = 0

			s_screen.fill(THECOLORS["white"])  # 刷屏

			s_screen.blit(si_food, (food_pos_x - 4, food_pos_y - 5))  # 刷食物图

			for i in bombs:
				s_screen.blit(si_bomb, ((i[0] - 2), (i[1] - 2)))

			for i in snakes:  # 刷蛇图
				s_screen.blit(si_snake, i)

			s_infoarea.fill(THECOLORS["gray"])
			pygame.draw.line(s_infoarea, THECOLORS["black"], (0, 0), (0, INFOAREA_HEIGHT), 3)
			s_infoarea.blit(sf_small_arial_level, (10, 5))
			s_infoarea.blit(sf_small_arial_ate, (10, 20))
			s_infoarea.blit(sf_small_arial_length, (10, 35))
			s_infoarea.blit(sf_small_arial_position, (10, 50))
			s_infoarea.blit(Lsf_small_arial_numbers_black[level], (65, 5))
			s_infoarea.blit(Lsf_small_arial_numbers_black[int(ate / 10)], (65, 20))
			s_infoarea.blit(Lsf_small_arial_numbers_black[ate % 10], (73, 20))
			s_screen.blit(s_infoarea, (PLAYGROUND_WIDTH, 0))
			pygame.display.flip()  # 更新屏
			c_frame = 0  # 更新一轮计数器

			if deadflag:
				f_gameover(s_screen, fps_clock, fps)
				return

		c_frame += 1
		fps_clock.tick(fps)

def f_gamestart(_s_screen, _fps_clock, _fps):
	while True:
		for event in pygame.event.get():  # 处理事件
			if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_q):  # 退出事件
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key == K_SPACE:  # 开始
				return

		_s_screen.fill(THECOLORS["white"])  # 刷白屏
		_s_screen.blit(sf_optima_caption, (81, 3))
		_s_screen.blit(si_gamestart, (93, 90))
		_s_screen.blit(sf_small_arial_gamestart, (62, 52))
		_s_screen.blit(sf_small_arial_scoreboard, (62, 70))
		pygame.display.flip()
		_fps_clock.tick(_fps)  # fps延迟

def f_gameover(_s_screen, _fps_clock, _fps):
	while True:
		for event in pygame.event.get():  # 处理事件
			if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_q:  # 退出事件
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key == K_r:  # 重新开始
				return

		_s_screen.fill(THECOLORS["white"])  # 刷屏
		_s_screen.blit(si_deadsnake, (80, 70))
		_s_screen.blit(sf_arial_gameover, (72, 20))  # 刷文字
		_s_screen.blit(sf_small_arial_restart, (92, 60))
		pygame.display.flip()  # 更新屏幕
		_fps_clock.tick(_fps)  # fps延迟

def f_scoreboard(_s_screen, _fps_clock, _fps):
	while True:
		for event in pygame.event.get():  # 处理事件
			if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_q:  # 退出事件
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key == K_r:  # 重新开始
				return
if __name__ == "__main__":  # 程序入口
	while True:
		main()
